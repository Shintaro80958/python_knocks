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

# %% colab={"base_uri": "https://localhost:8080/"} id="R0uwpFWdV_uF" executionInfo={"status": "ok", "timestamp": 1654454664405, "user_tz": -540, "elapsed": 17340, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="7fea641a-6cb8-46cf-9d7a-db0e0b4c9431"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="XuznOOOxWEVe" executionInfo={"status": "ok", "timestamp": 1654454664405, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/7章') #ここを変更。

# %% [markdown] id="Xj8jL5pdV_uH"
# # 7章 ロジスティクスネットワークの最適設計を行う10本ノック
#
# ここでは、最適化計算を行ういくつかのライブラリを用いて、最適化計算を実際に行っていきます。  
# そして、前章で用いたネットワーク可視化などの技術を駆使し、計算結果の妥当性を確認する方法についても学んでいきます。

# %% [markdown] id="x3FMg3UwV_uJ"
# ### ノック６１：輸送最適化問題を解いてみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="6jP1PkdnWRFP" executionInfo={"status": "ok", "timestamp": 1654454673371, "user_tz": -540, "elapsed": 8970, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="7ddfa0dd-4de9-413f-d7ab-1a9b62c38833"
# !pip install pulp
# !pip install ortoolpy

# %% colab={"base_uri": "https://localhost:8080/"} id="m2kqtjHxV_uJ" executionInfo={"status": "ok", "timestamp": 1654454674729, "user_tz": -540, "elapsed": 1362, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="40190724-e4b4-4416-eb1d-b3e126143d2d"
import numpy as np
import pandas as pd
from itertools import product
from pulp import LpVariable, lpSum, value
from ortoolpy import model_min, addvars, addvals

# データ読み込み
df_tc = pd.read_csv('trans_cost.csv', index_col="工場")
df_demand = pd.read_csv('demand.csv')
df_supply = pd.read_csv('supply.csv')

# 初期設定 #
np.random.seed(1)
nw = len(df_tc.index)
nf = len(df_tc.columns)
pr = list(product(range(nw), range(nf)))

# 数理モデル作成 #
m1 = model_min()
v1 = {(i,j):LpVariable('v%d_%d'%(i,j),lowBound=0) for i,j in pr}

m1 += lpSum(df_tc.iloc[i][j]*v1[i,j] for i,j in pr)
for i in range(nw):
    m1 += lpSum(v1[i,j] for j in range(nf)) <= df_supply.iloc[0][i]
for j in range(nf):
    m1 += lpSum(v1[i,j] for i in range(nw)) >= df_demand.iloc[0][j]
m1.solve()

# 総輸送コスト計算 #
df_tr_sol = df_tc.copy()
total_cost = 0
for k,x in v1.items():
    i,j = k[0],k[1]
    df_tr_sol.iloc[i][j] = value(x)
    total_cost += df_tc.iloc[i][j]*value(x)
    
print(df_tr_sol)
print("総輸送コスト:"+str(total_cost))

# %% [markdown] id="dU8yA4S2V_uK"
# ### ノック６２：最適輸送ルートをネットワークで確認しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 319} id="BKvk53gCV_uL" executionInfo={"status": "ok", "timestamp": 1654454675906, "user_tz": -540, "elapsed": 1179, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3618631e-b0e2-49e6-d538-df26369b517f"
import matplotlib.pyplot as plt
import networkx as nx

# データ読み込み
df_tr = df_tr_sol.copy()
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

# %% [markdown] id="-EPnlMTYV_uL"
# ### ノック６３：最適輸送ルートが制約条件内に収まっているかどうかを確認しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="cS7tzH_AV_uM" executionInfo={"status": "ok", "timestamp": 1654454675907, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3de1c03a-1c7f-4438-d351-40f230c78570"
# データ読み込み
df_demand = pd.read_csv('demand.csv')
df_supply = pd.read_csv('supply.csv')

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

print("需要条件計算結果:"+str(condition_demand(df_tr_sol,df_demand)))
print("供給条件計算結果:"+str(condition_supply(df_tr_sol,df_supply)))

# %% [markdown] id="Q9SoWqY2V_uN"
# ### ノック６４：生産計画に関するデータを読み込んでみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="YtOdUw7kV_uN" executionInfo={"status": "ok", "timestamp": 1654454676980, "user_tz": -540, "elapsed": 1078, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="bf46c083-3d6d-45bc-e57a-19e49a789fd7"
df_material = pd.read_csv('product_plan_material.csv', index_col="製品")
print(df_material)
df_profit = pd.read_csv('product_plan_profit.csv', index_col="製品")
print(df_profit)
df_stock = pd.read_csv('product_plan_stock.csv', index_col="項目")
print(df_stock)
df_plan = pd.read_csv('product_plan.csv', index_col="製品")
print(df_plan)


# %% [markdown] id="GiWLDQ8eV_uO"
# ### ノック６５：利益を計算する関数を作ってみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="l4lbZoEJV_uO" executionInfo={"status": "ok", "timestamp": 1654454676980, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5cbdaa16-924e-4551-eda5-6bdea9eea7bd"
# 利益計算関数
def product_plan(df_profit,df_plan):
    profit = 0
    for i in range(len(df_profit.index)):
        for j in range(len(df_plan.columns)):
            profit += df_profit.iloc[i][j]*df_plan.iloc[i][j]
    return profit

print("総利益:"+str(product_plan(df_profit,df_plan)))

# %% [markdown] id="0AAaOsFNV_uP"
# ### ノック６６：生産最適化問題を解いてみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="2oIyMKqtV_uQ" executionInfo={"status": "ok", "timestamp": 1654454676980, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="2fbe5340-907f-4628-e65e-bc23d8347ec6"
from pulp import LpVariable, lpSum, value
from ortoolpy import model_max, addvars, addvals


df = df_material.copy()
inv = df_stock

m = model_max()
v1 = {(i):LpVariable('v%d'%(i),lowBound=0) for i in range(len(df_profit))}
m += lpSum(df_profit.iloc[i]*v1[i] for i in range(len(df_profit)))
for i in range(len(df_material.columns)):
    m += lpSum(df_material.iloc[j,i]*v1[j] for j in range(len(df_profit)) ) <= df_stock.iloc[:,i]
m.solve()

df_plan_sol = df_plan.copy()
for k,x in v1.items():
    df_plan_sol.iloc[k] = value(x)
print(df_plan_sol)
print("総利益:"+str(value(m.objective)))


# %% [markdown] id="G9CZIeZhV_uQ"
# ### ノック６７：最適生産計画が制約条件内に収まっているかどうかを確認しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="8OJegFIlV_uQ" executionInfo={"status": "ok", "timestamp": 1654454676980, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="2fc77519-ca2f-4c98-bd0f-83e824ccbb27"
# 制約条件計算関数
def condition_stock(df_plan,df_material,df_stock):
    flag = np.zeros(len(df_material.columns))
    for i in range(len(df_material.columns)):  
        temp_sum = 0
        for j in range(len(df_material.index)):  
            temp_sum = temp_sum + df_material.iloc[j][i]*float(df_plan.iloc[j])
        if (temp_sum<=float(df_stock.iloc[0][i])):
            flag[i] = 1
        print(df_material.columns[i]+"  使用量:"+str(temp_sum)+", 在庫:"+str(float(df_stock.iloc[0][i])))
    return flag

print("制約条件計算結果:"+str(condition_stock(df_plan_sol,df_material,df_stock)))

# %% [markdown] id="GYrz3deLV_uQ"
# ### ノック６８：ロジスティクスネットワーク設計問題を解いてみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="EDlkUFDEV_uR" executionInfo={"status": "ok", "timestamp": 1654454677343, "user_tz": -540, "elapsed": 367, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ce91ccc3-bcd0-4642-fd59-c9e773c4d103"
製品 = list('AB')
需要地 = list('PQ')
工場 = list('XY')
レーン = (2,2)

# 輸送費表 #
tbdi = pd.DataFrame(((j,k) for j in 需要地 for k in 工場), columns=['需要地','工場'])
tbdi['輸送費'] = [1,2,3,1]
print(tbdi)

# 需要表 #
tbde = pd.DataFrame(((j,i) for j in 需要地 for i in 製品), columns=['需要地','製品'])
tbde['需要'] = [10,10,20,20]
print(tbde)

# 生産表 #
tbfa = pd.DataFrame(((k,l,i,0,np.inf) for k,nl in zip (工場,レーン) for l in range(nl) for i in 製品), 
                    columns=['工場','レーン','製品','下限','上限'])
tbfa['生産費'] = [1,np.nan,np.nan,1,3,np.nan,5,3]
tbfa.dropna(inplace=True)
tbfa.loc[4,'上限']=10
print(tbfa)

from ortoolpy import logistics_network
_, tbdi2, _ = logistics_network(tbde,tbdi,tbfa)
print(tbfa)
print(tbdi2)

# %% [markdown] id="MV9uujZsV_uR"
# ### ノック６９：最適ネットワークにおける輸送コストとその内訳を計算しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="kROAlkRWV_uR" executionInfo={"status": "ok", "timestamp": 1654454677343, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ef587b21-e79e-4d77-d06a-31b20ca21a02"
print(tbdi2)
trans_cost = 0
for i in range(len(tbdi2.index)):
    trans_cost += tbdi2["輸送費"].iloc[i]*tbdi2["ValX"].iloc[i]
print("総輸送コスト:"+str(trans_cost))

# %% [markdown] id="v0FrpxG4V_uR"
# ### ノック７０：最適ネットワークにおける生産コストとその内訳を計算しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="vASSxxKBV_uS" executionInfo={"status": "ok", "timestamp": 1654454677343, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="6a6162a5-a3e5-4c5c-ff85-d048695fd718"
print(tbfa)
product_cost = 0
for i in range(len(tbfa.index)):
    product_cost += tbfa["生産費"].iloc[i]*tbfa["ValY"].iloc[i]
print("総生産コスト:"+str(product_cost))

# %% id="dOQwS0jRXAsX" executionInfo={"status": "ok", "timestamp": 1654454677343, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
