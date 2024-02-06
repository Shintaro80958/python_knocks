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

# %% colab={"base_uri": "https://localhost:8080/"} id="KuX3for35gHE" executionInfo={"status": "ok", "timestamp": 1654454090336, "user_tz": -540, "elapsed": 22376, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ecdc85e3-8146-41ff-fdb6-1962802e6533"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="OZbzeizN6l8l" executionInfo={"status": "ok", "timestamp": 1654454090336, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所が異なるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/1章') #ここを変更。

# %% [markdown] id="HLi8pnEQ5gHG"
# # １章 ウェブの注文数を分析する１０本ノック
#
# ここでは、ある企業のECサイトでの商品の注文数の推移を分析していきます。  
# データの属性を理解し、分析をするためにデータを加工した後、  
# データの可視化を行うことで問題を発見していくプロセスを学びます。

# %% [markdown] id="9J3CTg9b5gHI"
# ### ノック１：データを読み込んでみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="xwc3wdQA5gHI" executionInfo={"status": "ok", "timestamp": 1654454091544, "user_tz": -540, "elapsed": 1211, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="870e9896-f914-428c-92f8-e694c416487c"
import pandas as pd
customer_master = pd.read_csv('customer_master.csv')
customer_master.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="0KZGbtKa5gHJ" executionInfo={"status": "ok", "timestamp": 1654454092689, "user_tz": -540, "elapsed": 1148, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a47a2abf-55e6-4489-8d4b-2cdb32526b99"
item_master = pd.read_csv('item_master.csv')
item_master.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="2FpXwPGH5gHK" executionInfo={"status": "ok", "timestamp": 1654454092689, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="9591b184-3383-4d21-ea30-6fee62ec5c65"
transaction_1 = pd.read_csv('transaction_1.csv')
transaction_1.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="9v_6vuUm5gHL" executionInfo={"status": "ok", "timestamp": 1654454093610, "user_tz": -540, "elapsed": 926, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="f7f153c3-009a-48a0-81bb-d97b1db3b719"
transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
transaction_detail_1.head()

# %% [markdown] id="J0OCYUez5gHL"
# ### ノック２：データを結合(ユニオン)してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="4nsJ7ON05gHL" executionInfo={"status": "ok", "timestamp": 1654454094189, "user_tz": -540, "elapsed": 581, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ff5bbb98-8b18-4a7b-9da2-c98ae6c641a5"
transaction_2 = pd.read_csv('transaction_2.csv')
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
transaction.head()

# %% colab={"base_uri": "https://localhost:8080/"} id="noeDj_aa5gHM" executionInfo={"status": "ok", "timestamp": 1654454094190, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="df505832-3503-469b-929e-8501c34c99d5"
print(len(transaction_1))
print(len(transaction_2))
print(len(transaction))

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="LikR5f6x5gHM" executionInfo={"status": "ok", "timestamp": 1654454094680, "user_tz": -540, "elapsed": 496, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="221f8b02-c013-4b95-9d71-edd153bba04d"
transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
transaction_detail=pd.concat([transaction_detail_1,transaction_detail_2], ignore_index=True)
transaction_detail.head()

# %% [markdown] id="zFNJ0oq05gHN"
# ### ノック３：売上データ同士を結合(ジョイン)してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="hHlWVx9W5gHN" executionInfo={"status": "ok", "timestamp": 1654454095170, "user_tz": -540, "elapsed": 494, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="757ce7cd-7b07-41e3-a1da-cea52842f099"
join_data = pd.merge(transaction_detail, transaction[["transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")
join_data.head()

# %% colab={"base_uri": "https://localhost:8080/"} id="YSAdJy7d5gHN" executionInfo={"status": "ok", "timestamp": 1654454095171, "user_tz": -540, "elapsed": 15, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="bb328742-21df-4b16-ef66-8f99044993ad"
print(len(transaction_detail))
print(len(transaction))
print(len(join_data))

# %% [markdown] id="7FaQaPI35gHO"
# ### ノック４：マスタデータを結合(ジョイン)してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 357} id="RXVLYCTg5gHO" executionInfo={"status": "ok", "timestamp": 1654454095171, "user_tz": -540, "elapsed": 14, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="7fee37db-6012-4ab0-cbcb-ae42239e66c6"
join_data = pd.merge(join_data, customer_master, on="customer_id", how="left")
join_data = pd.merge(join_data, item_master, on="item_id", how="left")
join_data.head()

# %% [markdown] id="ZebfeWkN5gHO"
# ### ノック5：必要なデータ列を作ろう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="Kzd6iNIk5gHO" executionInfo={"status": "ok", "timestamp": 1654454095172, "user_tz": -540, "elapsed": 14, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="357f9ad2-29b7-448b-c876-27f99e614b7a"
join_data["price"] = join_data["quantity"] * join_data["item_price"]
join_data[["quantity", "item_price","price"]].head()

# %% [markdown] id="JhRU0Sxz5gHO"
# ### ノック6：データ検算をしよう

# %% colab={"base_uri": "https://localhost:8080/"} id="fEwYRZhD5gHP" executionInfo={"status": "ok", "timestamp": 1654454095172, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="89c1e47b-6c53-40e5-9b9f-8c85789d3d5e"
print(join_data["price"].sum())
print(transaction["price"].sum())

# %% colab={"base_uri": "https://localhost:8080/"} id="S9_OrzEP5gHP" executionInfo={"status": "ok", "timestamp": 1654454095172, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ef85ed80-560e-4eb5-fd03-6f1458940ade"
join_data["price"].sum() == transaction["price"].sum()

# %% [markdown] id="dSF6_ncZ5gHP"
# ### ノック7：各種統計量を把握しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="sIZKIN2o5gHP" executionInfo={"status": "ok", "timestamp": 1654454095173, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="dd99cac1-2031-4629-dd73-a8a05df3fc59"
join_data.isnull().sum()

# %% colab={"base_uri": "https://localhost:8080/", "height": 300} id="4O4-z7J35gHP" executionInfo={"status": "ok", "timestamp": 1654454095173, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="8f332171-9ccb-4a81-8de1-413c9d9a93ef"
join_data.describe()

# %% colab={"base_uri": "https://localhost:8080/"} id="cJFH0m5B5gHP" executionInfo={"status": "ok", "timestamp": 1654454095173, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="6ead2ab1-7eb4-4db9-f9cd-85c7c3eeaf42"
print(join_data["payment_date"].min())
print(join_data["payment_date"].max())

# %% [markdown] id="zzFz2FF25gHQ"
# ### ノック8：月別でデータを集計してみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="LJ_ghgLW5gHQ" executionInfo={"status": "ok", "timestamp": 1654454095911, "user_tz": -540, "elapsed": 427, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="b715bdec-9954-4399-bc8a-1f23f3d09812"
join_data.dtypes

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="1WNDIpOd5gHQ" executionInfo={"status": "ok", "timestamp": 1654454095912, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="358a20f5-a4e1-4066-a4f3-702289f51240"
join_data["payment_date"] = pd.to_datetime(join_data["payment_date"])
join_data["payment_month"] = join_data["payment_date"].dt.strftime("%Y%m")
join_data[["payment_date", "payment_month"]].head()

# %% colab={"base_uri": "https://localhost:8080/"} id="SXrvjXk35gHQ" executionInfo={"status": "ok", "timestamp": 1654454096228, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="aba5b279-9010-4cd9-9d04-fa5e1fea0f79"
join_data.groupby("payment_month").sum()["price"]

# %% [markdown] id="7HosQXVr5gHQ"
# ### ノック9：月別、商品別でデータを集計してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 1000} id="zDz8eZPR5gHQ" executionInfo={"status": "ok", "timestamp": 1654454096664, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="83a2a8c4-0173-4349-e1fc-b4680f31e1c6"
join_data.groupby(["payment_month","item_name"]).sum()[["price", "quantity"]]

# %% colab={"base_uri": "https://localhost:8080/", "height": 269} id="X4ixXCoV5gHQ" executionInfo={"status": "ok", "timestamp": 1654454097244, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ef5f4eea-b1af-440c-894f-b9a367a45871"
pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price', 'quantity'], aggfunc='sum')

# %% [markdown] id="gTpGRRSu5gHQ"
# ### ノック10：商品別の売上推移を可視化してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 237} id="msJiUwVn5gHQ" executionInfo={"status": "ok", "timestamp": 1654454097636, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3db23822-d6c5-47b4-8291-448fa2a1b29a"
graph_data = pd.pivot_table(join_data, index='payment_month', columns='item_name', values='price', aggfunc='sum')
graph_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 294} id="GB7cWkVC5gHR" executionInfo={"status": "ok", "timestamp": 1654454098671, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="60037b7e-7498-462b-b6e5-d9894bacda85"
import matplotlib.pyplot as plt
# %matplotlib inline
plt.plot(list(graph_data.index), graph_data["PC-A"], label='PC-A')
plt.plot(list(graph_data.index), graph_data["PC-B"], label='PC-B')
plt.plot(list(graph_data.index), graph_data["PC-C"], label='PC-C')
plt.plot(list(graph_data.index), graph_data["PC-D"], label='PC-D')
plt.plot(list(graph_data.index), graph_data["PC-E"], label='PC-E')
plt.legend()  

# %% id="XGN4ymwjIkmu"
