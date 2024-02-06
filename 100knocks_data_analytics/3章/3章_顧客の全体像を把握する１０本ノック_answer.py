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

# %% colab={"base_uri": "https://localhost:8080/"} id="au9vKZJ5BRFa" executionInfo={"status": "ok", "timestamp": 1654454298821, "user_tz": -540, "elapsed": 22377, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="4afd137a-7afe-4254-83fb-b3fb025fd7a4"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="oBZLWhwrBUPE" executionInfo={"status": "ok", "timestamp": 1654454317703, "user_tz": -540, "elapsed": 284, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/3章') #ここを変更。

# %% [markdown] id="5XUaDt_zBRFc"
# # 3章 顧客の全体像を把握する１０本ノック
#
# ここでは、スポーツジムの会員データを使って顧客の行動を分析していきます。  
# これまでと同様にまずはデータを理解し、加工した後、  
# 顧客の行動データを分析していきましょう。  
# ここでは、機械学習に向けての初期分析を行います。

# %% [markdown] id="y2AmyqeEBRFe"
# ### ノック21：データを読み込んで把握しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 224} id="cp0J7oRuBRFe" executionInfo={"status": "ok", "timestamp": 1654454319725, "user_tz": -540, "elapsed": 1324, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5a8e96fb-ad84-4219-bc9e-fedc12bcc4f4"
import pandas as pd
uselog = pd.read_csv('use_log.csv')
print(len(uselog))
uselog.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 224} id="XEwhfrrCBRFf" executionInfo={"status": "ok", "timestamp": 1654454320070, "user_tz": -540, "elapsed": 347, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="72896e90-9741-406d-94d6-191e8a2f7a36"
customer = pd.read_csv('customer_master.csv')
print(len(customer))
customer.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 161} id="dbjijJO0BRFg" executionInfo={"status": "ok", "timestamp": 1654454320071, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3c1a483b-e81f-4dad-b8d2-e3e0b07e8ee2"
class_master = pd.read_csv('class_master.csv')
print(len(class_master))
class_master.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 161} id="6KCMGDC1BRFg" executionInfo={"status": "ok", "timestamp": 1654454320322, "user_tz": -540, "elapsed": 256, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3dc70126-c85f-49b4-8c5e-6751dd492897"
campaign_master = pd.read_csv('campaign_master.csv')
print(len(campaign_master))
campaign_master.head()

# %% [markdown] id="_Z_ymg2CBRFh"
# ### ノック22：顧客データを整形しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="UU69bO5IBRFh" executionInfo={"status": "ok", "timestamp": 1654454320323, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="36aa216e-3a00-48f6-afe1-08db0b41085c"
customer_join = pd.merge(customer, class_master, on="class", how="left")
customer_join = pd.merge(customer_join, campaign_master, on="campaign_id", how="left")
customer_join.head()

# %% colab={"base_uri": "https://localhost:8080/"} id="K0Nkx9oJBRFh" executionInfo={"status": "ok", "timestamp": 1654454320323, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="eca12630-c32a-45f6-ffc9-8d4423c3bb0e"
print(len(customer))
print(len(customer_join))

# %% colab={"base_uri": "https://localhost:8080/"} id="8SLPK1wwBRFi" executionInfo={"status": "ok", "timestamp": 1654454320608, "user_tz": -540, "elapsed": 289, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="672d57bd-de0c-4eec-faae-1631128e7313"
customer_join.isnull().sum()

# %% [markdown] id="ZTy-WwpLBRFi"
# ### ノック23：顧客データの基礎集計をしよう

# %% colab={"base_uri": "https://localhost:8080/"} id="F9uAJc2XBRFi" executionInfo={"status": "ok", "timestamp": 1654454320912, "user_tz": -540, "elapsed": 306, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="fb4eee13-0ea1-497a-eb49-dab59fd52704"
customer_join.groupby("class_name").count()["customer_id"]

# %% colab={"base_uri": "https://localhost:8080/"} id="u5__5hG0BRFj" executionInfo={"status": "ok", "timestamp": 1654454320912, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="108be869-426e-4244-e41f-f7fda1070a73"
customer_join.groupby("campaign_name").count()["customer_id"]

# %% colab={"base_uri": "https://localhost:8080/"} id="AMoyFFInBRFj" executionInfo={"status": "ok", "timestamp": 1654454320912, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3ac1b12b-fa0a-4aa6-8fa4-f18642e485a2"
customer_join.groupby("gender").count()["customer_id"]

# %% colab={"base_uri": "https://localhost:8080/"} id="gaQstHOOBRFk" executionInfo={"status": "ok", "timestamp": 1654454321494, "user_tz": -540, "elapsed": 331, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="02267e65-5f20-4723-f26d-f98fb6f92b35"
customer_join.groupby("is_deleted").count()["customer_id"]

# %% colab={"base_uri": "https://localhost:8080/"} id="HAVsMIaFBRFk" executionInfo={"status": "ok", "timestamp": 1654454321495, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="656d7c7c-cb21-4114-87aa-2a03aabeb5dd"
customer_join["start_date"] = pd.to_datetime(customer_join["start_date"])
customer_start = customer_join.loc[customer_join["start_date"]>pd.to_datetime("20180401")]
print(len(customer_start))

# %% [markdown] id="aYGClyHvBRFl"
# ### ノック24：最新顧客データの基礎集計をしよう

# %% colab={"base_uri": "https://localhost:8080/"} id="XyyNbrLZBRFl" executionInfo={"status": "ok", "timestamp": 1654454321736, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5d56df29-5ca9-433a-e3b1-288de5f213fd"
customer_join["end_date"] = pd.to_datetime(customer_join["end_date"])
customer_newer = customer_join.loc[(customer_join["end_date"]>=pd.to_datetime("20190331"))|(customer_join["end_date"].isna())]
print(len(customer_newer))
customer_newer["end_date"].unique()

# %% colab={"base_uri": "https://localhost:8080/"} id="TsAsmzmHBRFl" executionInfo={"status": "ok", "timestamp": 1654454322007, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="325effae-a7db-45dd-92db-bef7d31fbd90"
customer_newer.groupby("class_name").count()["customer_id"]

# %% colab={"base_uri": "https://localhost:8080/"} id="DDnjPPjrBRFm" executionInfo={"status": "ok", "timestamp": 1654454322340, "user_tz": -540, "elapsed": 334, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0c01b3c2-bd9c-41de-9a63-86bffeb63a23"
customer_newer.groupby("campaign_name").count()["customer_id"]

# %% colab={"base_uri": "https://localhost:8080/"} id="Pm4jF_QRBRFm" executionInfo={"status": "ok", "timestamp": 1654454322667, "user_tz": -540, "elapsed": 328, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="2004b8bb-0d3f-4271-d6f3-38f8a5a75477"
customer_newer.groupby("gender").count()["customer_id"]

# %% [markdown] id="uya534UcBRFm"
# ### ノック25：利用履歴データを集計しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="29SkjK4YBRFn" executionInfo={"status": "ok", "timestamp": 1654454323776, "user_tz": -540, "elapsed": 1111, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a6393359-5d81-4a2e-8cc0-a6d1200cf365"
uselog["usedate"] = pd.to_datetime(uselog["usedate"])
uselog["年月"] = uselog["usedate"].dt.strftime("%Y%m")
uselog_months = uselog.groupby(["年月","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]
uselog_months.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="aKOzYsP7BRFn" executionInfo={"status": "ok", "timestamp": 1654454326533, "user_tz": -540, "elapsed": 2760, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a8ab2336-ee8e-4b1b-852a-2b8134c4aec0"
uselog_customer = uselog_months.groupby("customer_id").agg(["mean", "median", "max", "min" ])["count"]
uselog_customer = uselog_customer.reset_index(drop=False)
uselog_customer.head()

# %% [markdown] id="GM8fykvCBRFn"
# ### ノック26：利用履歴データから定期利用フラグを作成しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="WsSdFz43BRFn" executionInfo={"status": "ok", "timestamp": 1654454326534, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="db93e84e-7491-41f5-e0d6-09752130d00d"
uselog["weekday"] = uselog["usedate"].dt.weekday
uselog_weekday = uselog.groupby(["customer_id","年月","weekday"], as_index=False).count()[["customer_id","年月", "weekday","log_id"]]
uselog_weekday.rename(columns={"log_id":"count"}, inplace=True)
uselog_weekday.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 422} id="r4BBZiXKBRFn" executionInfo={"status": "ok", "timestamp": 1654454327244, "user_tz": -540, "elapsed": 715, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5387150c-a6b8-4e6e-c6ed-818d800d87ed"
uselog_weekday = uselog_weekday.groupby("customer_id",as_index=False).max()[["customer_id", "count"]]
uselog_weekday["routine_flg"] = 0
uselog_weekday["routine_flg"] = uselog_weekday["routine_flg"].where(uselog_weekday["count"]<4, 1)
uselog_weekday.head()

# %% [markdown] id="nuNNyCeRBRFn"
# ### ノック27：顧客データと利用履歴データを結合しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 357} id="MaJDg_2lBRFo" executionInfo={"status": "ok", "timestamp": 1654454327245, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="71d20c6b-c3be-4b40-d543-5c0ec0792d10"
customer_join = pd.merge(customer_join, uselog_customer, on="customer_id", how="left")
customer_join = pd.merge(customer_join, uselog_weekday[["customer_id", "routine_flg"]], on="customer_id", how="left")
customer_join.head()

# %% colab={"base_uri": "https://localhost:8080/"} id="Wcq8NDauBRFo" executionInfo={"status": "ok", "timestamp": 1654454327245, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="8800da6e-866b-439c-9df5-db6b5676b87e"
customer_join.isnull().sum()

# %% [markdown] id="j_ZYT9fGBRFo"
# ### ノック28：会員期間を計算しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 357} id="mNkAyU2tBRFo" executionInfo={"status": "ok", "timestamp": 1654454329421, "user_tz": -540, "elapsed": 2183, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="06bb4b6c-2bd5-4f66-cc66-beb62fbc6b1b"
from dateutil.relativedelta import relativedelta
customer_join["calc_date"] = customer_join["end_date"]
customer_join["calc_date"] = customer_join["calc_date"].fillna(pd.to_datetime("20190430"))
customer_join["membership_period"] = 0
for i in range(len(customer_join)):
    delta = relativedelta(customer_join["calc_date"].iloc[i], customer_join["start_date"].iloc[i])
    customer_join.loc[i,"membership_period"] = delta.years*12 + delta.months
customer_join.head()

# %% [markdown] id="cKsHvMr2BRFo"
# ### ノック29：顧客行動の各種統計量を把握しよう

# %% id="nZR-dOQMBRFo" outputId="bbfce03f-74c9-47ba-98d8-79b08dc653b0" colab={"base_uri": "https://localhost:8080/", "height": 300} executionInfo={"status": "ok", "timestamp": 1654454329423, "user_tz": -540, "elapsed": 18, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
customer_join[["mean", "median", "max", "min"]].describe()

# %% id="tCKjMpELBRFo" outputId="db210f50-05d7-4279-ceb7-11ec27d629b8" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1654454329424, "user_tz": -540, "elapsed": 15, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
customer_join.groupby("routine_flg").count()["customer_id"]

# %% id="iOVksiTDBRFp" outputId="910c3896-ed75-4c93-9c32-c79d19608807" colab={"base_uri": "https://localhost:8080/", "height": 319} executionInfo={"status": "ok", "timestamp": 1654454329899, "user_tz": -540, "elapsed": 487, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
import matplotlib.pyplot as plt
# %matplotlib inline
plt.hist(customer_join["membership_period"])

# %% [markdown] id="YuFO2RAPBRFp"
# ### ノック30：退会ユーザーと継続ユーザーの違いを把握しよう

# %% id="yiDQWQfJBRFp" outputId="a69349b5-8984-446b-9a5a-915f99053a7d" colab={"base_uri": "https://localhost:8080/", "height": 300} executionInfo={"status": "ok", "timestamp": 1654454329900, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
customer_end = customer_join.loc[customer_join["is_deleted"]==1]
customer_end.describe()

# %% id="gj4GKHhrBRFp" outputId="5eac6b4d-7bfa-4d99-f7fc-46ac859021b6" colab={"base_uri": "https://localhost:8080/", "height": 300} executionInfo={"status": "ok", "timestamp": 1654454329900, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
customer_stay = customer_join.loc[customer_join["is_deleted"]==0]
customer_stay.describe()

# %% id="6xxzqcjDBRFp" executionInfo={"status": "ok", "timestamp": 1654454330112, "user_tz": -540, "elapsed": 217, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
customer_join.to_csv("customer_join.csv", index=False)

# %% id="-djl9-3NMPjU"
