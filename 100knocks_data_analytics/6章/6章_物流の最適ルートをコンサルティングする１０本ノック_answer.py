# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% colab={"base_uri": "https://localhost:8080/"} id="aZB-AcguUH6H" executionInfo={"status": "ok", "timestamp": 1674037418767, "user_tz": -540, "elapsed": 26100, "user": {"displayName": "Yuma Matsuda", "userId": "07185311855020035375"}} outputId="d922fce0-d35c-471b-aada-9e14bf24273c"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="se2ZI_UbULll" executionInfo={"status": "ok", "timestamp": 1674037419215, "user_tz": -540, "elapsed": 453, "user": {"displayName": "Yuma Matsuda", "userId": "07185311855020035375"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/6章') #ここを変更。

# %% [markdown] id="iIsnfNF3UH6K"
# # 6章 物流の最適ルートをコンサルティングする１０本ノック
#
# ここでは、「物流」の基礎となる「輸送最適化」を検討するにあたっての基礎的な技術を習得します。  
# 実際の物流データからネットワーク構造を可視化する方法について学び、最適な物流計画を立案する流れを学んでいきます。

# %% [markdown] id="vaCMey7kUH6L"
# ### ノック５１：物流に関するデータを読み込んでみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 332} id="13GPBVYzUH6M" executionInfo={"status": "ok", "timestamp": 1674037445257, "user_tz": -540, "elapsed": 1107, "user": {"displayName": "Yuma Matsuda", "userId": "07185311855020035375"}} outputId="2a99f7da-8533-4678-cb64-34b5cf1a4111"
import pandas as pd

# 工場データの読み込み
factories = pd.read_csv("tbl_factory.csv", index_col=0)
factories

# %% colab={"base_uri": "https://localhost:8080/", "height": 269} id="lRdM0s_FUH6N" executionInfo={"status": "ok", "timestamp": 1654454574595, "user_tz": -540, "elapsed": 657, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="803ab0dc-cd7a-49d1-e95f-4219e2c9ab40"
# 倉庫データの読み込み
warehouses = pd.read_csv("tbl_warehouse.csv", index_col=0)
warehouses

# %% colab={"base_uri": "https://localhost:8080/", "height": 237} id="tt6pQ2jMUH6N" executionInfo={"status": "ok", "timestamp": 1654454574843, "user_tz": -540, "elapsed": 250, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="41e22eb9-c3a5-4f72-b5ca-48772bf2c80e"
# コストテーブル
cost = pd.read_csv("rel_cost.csv", index_col=0)
cost.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 237} id="Z0rqzGskUH6O" executionInfo={"status": "ok", "timestamp": 1654454575238, "user_tz": -540, "elapsed": 397, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="367c979d-14a7-4386-f8b0-f95ee1e82f08"
# 輸送トランザクションテーブル
trans = pd.read_csv("tbl_transaction.csv", index_col=0)
trans.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="sk2i0u8zUH6P" executionInfo={"status": "ok", "timestamp": 1654454575239, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="c2136184-6f2b-4289-ebc3-293611f5a830"
# トランザクションテーブルに各テーブルをジョインする
# コストデータを付与
join_data = pd.merge(trans, cost, left_on=["ToFC","FromWH"], right_on=["FCID","WHID"], how="left")
join_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="nuC2EsquUH6P" executionInfo={"status": "ok", "timestamp": 1654454575239, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="6c37caaf-7133-4fcb-dbc7-cf7e682bb74a"
# 工場情報を付与
join_data = pd.merge(join_data, factories, left_on="ToFC", right_on="FCID", how="left")
join_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="Wz1vIeJxUH6Q" executionInfo={"status": "ok", "timestamp": 1654454575239, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="44aca1d9-f818-41b7-b6ed-2a86807d685e"
# 倉庫情報を付与
join_data = pd.merge(join_data, warehouses, left_on="FromWH", right_on="WHID", how="left")
# カラムの並び替え
join_data = join_data[["TransactionDate","Quantity","Cost","ToFC","FCName","FCDemand","FromWH","WHName","WHSupply","WHRegion"]]
join_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="RlRO6csNUH6Q" executionInfo={"status": "ok", "timestamp": 1654454575240, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="69bef894-c250-4791-f109-07cbd930363c"
# 関東データを抽出
kanto = join_data.loc[join_data["WHRegion"]=="関東"]
kanto.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="Q5un6pJ1UH6R" executionInfo={"status": "ok", "timestamp": 1654454575509, "user_tz": -540, "elapsed": 279, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="09cd39d7-8f90-4900-969c-82cf68ecf232"
# 東北データを抽出
tohoku = join_data.loc[join_data["WHRegion"]=="東北"]
tohoku.head()

# %% [markdown] id="lLl_dVSLUH6R"
# ### ノック５２：現状の輸送量、コストを確認してみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="_oTdRjQWUH6R" executionInfo={"status": "ok", "timestamp": 1654454575509, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="61bc0662-4655-4940-f11c-ede8c1e5ae72"
# 支社のコスト合計を算出
print("関東支社の総コスト: " + str(kanto["Cost"].sum()) + "万円")
print("東北支社の総コスト: " + str(tohoku["Cost"].sum()) + "万円")

# %% colab={"base_uri": "https://localhost:8080/"} id="XcVOQojDUH6S" executionInfo={"status": "ok", "timestamp": 1654454575510, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5b52a1ab-4742-4071-960f-803db2c89ac6"
# 支社の総輸送個数
print("関東支社の総部品輸送個数: " + str(kanto["Quantity"].sum()) + "個")
print("東北支社の総部品輸送個数: " + str(tohoku["Quantity"].sum()) + "個")

# %% colab={"base_uri": "https://localhost:8080/"} id="XJ7CVhmPUH6S" executionInfo={"status": "ok", "timestamp": 1654454575510, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="1b480dc8-0282-4b03-9c26-79341ec82bd9"
# 部品一つ当たりの輸送コスト
tmp = (kanto["Cost"].sum() / kanto["Quantity"].sum()) * 10000
print("関東支社の部品１つ当たりの輸送コスト: " + str(int(tmp)) + "円")
tmp = (tohoku["Cost"].sum() / tohoku["Quantity"].sum()) * 10000
print("東北支社の部品１つ当たりの輸送コスト: " + str(int(tmp)) + "円")

# %% colab={"base_uri": "https://localhost:8080/"} id="HjnbaQ7LUH6S" executionInfo={"status": "ok", "timestamp": 1654454575510, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="522493c7-3dc4-4b9c-abc3-3e9dc14921d6"
# コストテーブルを支社ごとに集計
cost_chk = pd.merge(cost, factories, on="FCID", how="left")
# 平均
print("東京支社の平均輸送コスト：" + str(cost_chk["Cost"].loc[cost_chk["FCRegion"]=="関東"].mean()) + "万円")
print("東北支社の平均輸送コスト：" + str(cost_chk["Cost"].loc[cost_chk["FCRegion"]=="東北"].mean()) + "万円")

# %% [markdown] id="9mmip18YUH6S"
# ### ノック５３：ネットワークを可視化してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 319} id="d0AyUAUOUH6T" executionInfo={"status": "ok", "timestamp": 1674037462207, "user_tz": -540, "elapsed": 722, "user": {"displayName": "Yuma Matsuda", "userId": "07185311855020035375"}} outputId="13802e1d-5746-4f13-9c87-34c5dea3a9fb"
import networkx as nx
import matplotlib.pyplot as plt

# グラフオブジェクトの作成
G=nx.Graph()

# 頂点の設定
G.add_node("nodeA")
G.add_node("nodeB")
G.add_node("nodeC")

# 辺の設定
G.add_edge("nodeA","nodeB")
G.add_edge("nodeA","nodeC")
G.add_edge("nodeB","nodeC")

# 座標の設定
pos={}
pos["nodeA"]=(0,0)
pos["nodeB"]=(1,1)
pos["nodeC"]=(0,1)

# 描画
nx.draw(G,pos)

# 表示
plt.show()

# %% [markdown] id="S2GHuv8sUH6T"
# ### ノック５４：ネットワークにノードを追加してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 319} id="AkbymMZ-UH6T" executionInfo={"status": "ok", "timestamp": 1654454576194, "user_tz": -540, "elapsed": 293, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="9fb72e03-3496-40f1-a877-6e6578624e35"
# グラフオブジェクトの作成．
G=nx.Graph()

# 頂点の設定
G.add_node("nodeA")
G.add_node("nodeB")
G.add_node("nodeC")
G.add_node("nodeD")

# 辺の設定
G.add_edge("nodeA","nodeB")
G.add_edge("nodeA","nodeC")
G.add_edge("nodeB","nodeC")
G.add_edge("nodeA","nodeD")

# 座標の設定
pos={}
pos["nodeA"]=(0,0)
pos["nodeB"]=(1,1)
pos["nodeC"]=(0,1)
pos["nodeD"]=(1,0)

# 描画
nx.draw(G,pos, with_labels=True)

# 表示
plt.show()

# %% [markdown] id="eZUO7LE8UH6U"
# ### ノック５５：ルートの重みづけを実施しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 319} id="z5wNcHBxUH6U" executionInfo={"status": "ok", "timestamp": 1674038306154, "user_tz": -540, "elapsed": 945, "user": {"displayName": "Yuma Matsuda", "userId": "07185311855020035375"}} outputId="d5d5dd09-e37c-4307-a6c8-7c9804562f4e"
import numpy as np

# データ読み込み
df_w = pd.read_csv('network_weight.csv')
df_p = pd.read_csv('network_pos.csv')

# グラフオブジェクトの作成
G = nx.Graph()

# 頂点の設定
for i in range(len(df_w.columns)):
    G.add_node(df_w.columns[i])

# 辺の設定&エッジの重みのリスト化
size = 10
edge_weights = []
num_pre = 0
for i in range(len(df_w.columns)):
    for j in range(len(df_w.columns)):
        if not (i==j):
            # 辺の追加
            G.add_edge(df_w.columns[i],df_w.columns[j])
            if num_pre<len(G.edges):
              num_pre = len(G.edges)
              # エッジの重みの追加
              edge_weights.append(df_w.iloc[i][j]*size)

# 座標の設定
pos = {}
for i in range(len(df_w.columns)):
    node = df_w.columns[i]
    pos[node] = (df_p[node][0],df_p[node][1])

# 描画
nx.draw(G, pos, with_labels=True,font_size=16, node_size = 1000, node_color='k', font_color='w', width=edge_weights)

# 表示
plt.show()

# %% [markdown] id="Smcc9lKLUH6U"
# ### ノック５６：輸送ルート情報を読み込んでみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 175} id="BHo0y61pUH6V" executionInfo={"status": "ok", "timestamp": 1654454577916, "user_tz": -540, "elapsed": 509, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="1108ea30-e41d-42e9-e388-9f7e85ef33f9"
# データ読み込み
df_tr = pd.read_csv('trans_route.csv', index_col="工場")
df_tr.head()

# %% [markdown] id="KfXnwdoVUH6V"
# ### ノック５７：輸送ルート情報からネットワークを可視化してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 319} id="MhBr94CqUH6V" executionInfo={"status": "ok", "timestamp": 1654454578344, "user_tz": -540, "elapsed": 431, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5aab1d6a-d612-420b-9c5e-65b1ed0c67d0"
# データ読み込み
df_tr = pd.read_csv('trans_route.csv', index_col="工場")
df_pos = pd.read_csv('trans_route_pos.csv')


# グラフオブジェクトの作成
G = nx.Graph()

# 頂点の設定
for i in range(len(df_pos.columns)):
    G.add_node(df_pos.columns[i])

# 辺の設定&エッジの重みのリスト化
num_pre = 0
edge_weights = []
size = 0.1
for i in range(len(df_pos.columns)):
    for j in range(len(df_pos.columns)):
        if not (i==j):
            # 辺の追加
            G.add_edge(df_pos.columns[i],df_pos.columns[j])
            # エッジの重みの追加
            if num_pre<len(G.edges):
                num_pre = len(G.edges)
                weight = 0
                if (df_pos.columns[i] in df_tr.columns)and(df_pos.columns[j] in df_tr.index):
                    if df_tr[df_pos.columns[i]][df_pos.columns[j]]:
                        weight = df_tr[df_pos.columns[i]][df_pos.columns[j]]*size
                elif(df_pos.columns[j] in df_tr.columns)and(df_pos.columns[i] in df_tr.index):
                    if df_tr[df_pos.columns[j]][df_pos.columns[i]]:
                        weight = df_tr[df_pos.columns[j]][df_pos.columns[i]]*size
                edge_weights.append(weight)
                

# 座標の設定
pos = {}
for i in range(len(df_pos.columns)):
    node = df_pos.columns[i]
    pos[node] = (df_pos[node][0],df_pos[node][1])
    
# 描画
nx.draw(G, pos, with_labels=True,font_size=16, node_size = 1000, node_color='k', font_color='w', width=edge_weights)

# 表示
plt.show()


# %% [markdown] id="7DiKlZg-UH6V"
# ### ノック５８：輸送コスト関数を作成しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="qvsq-3UiUH6V" executionInfo={"status": "ok", "timestamp": 1654454578617, "user_tz": -540, "elapsed": 275, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="167f6764-f0b9-4a99-d4db-c2f5cb818143"
# データ読み込み
df_tr = pd.read_csv('trans_route.csv', index_col="工場")
df_tc = pd.read_csv('trans_cost.csv', index_col="工場")

# 輸送コスト関数
def trans_cost(df_tr,df_tc):
    cost = 0
    for i in range(len(df_tc.index)):
        for j in range(len(df_tr.columns)):
            cost += df_tr.iloc[i][j]*df_tc.iloc[i][j]
    return cost

print("総輸送コスト:"+str(trans_cost(df_tr,df_tc)))


# %% [markdown] id="YQKxYvrsUH6V"
# ### ノック５９：制約条件を作ってみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="i_0neuLmUH6V" executionInfo={"status": "ok", "timestamp": 1654454579363, "user_tz": -540, "elapsed": 748, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="bbd1d0c0-2ff9-4eb5-b16e-4d1376d4fc94"
# データ読み込み
df_tr = pd.read_csv('trans_route.csv', index_col="工場")
df_demand = pd.read_csv('demand.csv')
df_supply = pd.read_csv('supply.csv')

# 需要側の制約条件
for i in range(len(df_demand.columns)):
    temp_sum = sum(df_tr[df_demand.columns[i]])
    print(str(df_demand.columns[i])+"への輸送量:"+str(temp_sum)+" (需要量:"+str(df_demand.iloc[0][i])+")")
    if temp_sum>=df_demand.iloc[0][i]:
        print("需要量を満たしています。")
    else:
        print("需要量を満たしていません。輸送ルートを再計算して下さい。")

# 供給側の制約条件
for i in range(len(df_supply.columns)):
    temp_sum = sum(df_tr.loc[df_supply.columns[i]])
    print(str(df_supply.columns[i])+"からの輸送量:"+str(temp_sum)+" (供給限界:"+str(df_supply.iloc[0][i])+")")
    if temp_sum<=df_supply.iloc[0][i]:
        print("供給限界の範囲内です。")
    else:
        print("供給限界を超過しています。輸送ルートを再計算して下さい。")



# %% [markdown] id="-p3zlMSeUH6W"
# ### ノック６０：輸送ルートを変更して、輸送コスト関数の変化を確認しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="EU7rR3GYUH6W" executionInfo={"status": "ok", "timestamp": 1654454580057, "user_tz": -540, "elapsed": 696, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3d1a7223-e31c-4c7f-c671-19042102e26a"
# データ読み込み
df_tr_new = pd.read_csv('trans_route_new.csv', index_col="工場")
print(df_tr_new)

# 総輸送コスト再計算 
print("総輸送コスト(変更後):"+str(trans_cost(df_tr_new,df_tc)))

# 制約条件計算関数
# 需要側
def condition_demand(df_tr,df_demand):
    flag = np.zeros(len(df_demand.columns))
    for i in range(len(df_demand.columns)):
        temp_sum = sum(df_tr[df_demand.columns[i]])
        if (temp_sum>=df_demand.iloc[0][i]):
            flag[i] = 1
    return flag
            
# 供給側
def condition_supply(df_tr,df_supply):
    flag = np.zeros(len(df_supply.columns))
    for i in range(len(df_supply.columns)):
        temp_sum = sum(df_tr.loc[df_supply.columns[i]])
        if temp_sum<=df_supply.iloc[0][i]:
            flag[i] = 1
    return flag

print("需要条件計算結果:"+str(condition_demand(df_tr_new,df_demand)))
print("供給条件計算結果:"+str(condition_supply(df_tr_new,df_supply)))

# %% id="Zm6-a20loGmI"
