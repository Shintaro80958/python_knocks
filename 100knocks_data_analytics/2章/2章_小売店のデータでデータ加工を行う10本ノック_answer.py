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

# %% colab={"base_uri": "https://localhost:8080/"} id="CQhZLbtQAeEI" executionInfo={"status": "ok", "timestamp": 1654454198585, "user_tz": -540, "elapsed": 20582, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="66c327f0-77b0-4dfa-a064-bd8f35ea88c8"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="vF_JshRtAfOp" executionInfo={"status": "ok", "timestamp": 1654454202637, "user_tz": -540, "elapsed": 249, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/2章') #ここを変更。

# %% [markdown] id="9H1wpviFAbIq"
# # ２章　小売店のデータでデータ加工を行う１０本ノック
#
# 本章では、ある小売店の売上履歴と顧客台帳データを用いて、データ分析の素地となる「データの加工」を習得することが目的です。
# 実際の現場データは手入力のExcel等、決して綺麗なデータではない事が多いため、
# データの揺れや整合性の担保など、汚いデータを取り扱うデータ加工を主体に進めて行きます。

# %% [markdown] id="JY-0mpyyAbIt"
# ### ノック１１：データを読み込んでみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="qi6XXxsyAbIu" executionInfo={"status": "ok", "timestamp": 1654454207426, "user_tz": -540, "elapsed": 1243, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="f4b98877-cf59-4201-8c30-932e87e8cc1e"
import pandas as pd
uriage_data = pd.read_csv("uriage.csv")
uriage_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="0NfqK54_AbIv" executionInfo={"status": "ok", "timestamp": 1654454208472, "user_tz": -540, "elapsed": 1049, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0b7471a4-5049-48d5-d15e-67654a13d988"
kokyaku_data = pd.read_excel("kokyaku_daicho.xlsx")
kokyaku_data.head()

# %% [markdown] id="-kiPZP1AAbIv"
# ### ノック１２：データの揺れを見てみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="YpYFUtvFAbIw" executionInfo={"status": "ok", "timestamp": 1654454208472, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="22b7a334-5473-4c92-c1a2-213a049a5354"
uriage_data["item_name"].head()

# %% colab={"base_uri": "https://localhost:8080/"} id="wrzVsWI3AbIw" executionInfo={"status": "ok", "timestamp": 1654454208473, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="fad08f77-8e92-45f6-d0af-534dae279b4b"
uriage_data["item_price"].head()

# %% [markdown] id="6j4JAl_uAbIx"
# ### ノック１３：データに揺れがあるまま集計しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 391} id="N5pLAkwZAbIy" executionInfo={"status": "ok", "timestamp": 1654454208473, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="83c0a027-270f-4966-dbe3-44634c512162"
uriage_data["purchase_date"] = pd.to_datetime(uriage_data["purchase_date"])
uriage_data["purchase_month"] = uriage_data["purchase_date"].dt.strftime("%Y%m")
res = uriage_data.pivot_table(index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
res

# %% colab={"base_uri": "https://localhost:8080/", "height": 391} id="d4MEUWc8AbIy" executionInfo={"status": "ok", "timestamp": 1654454208473, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="dc563e84-fee8-4643-8e1c-052540b1f2b8"
res = uriage_data.pivot_table(index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
res

# %% [markdown] id="zaZUByOlAbIz"
# ### ノック１４：商品名の揺れを補正しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="Pn1xHZf-AbIz" executionInfo={"status": "ok", "timestamp": 1654454208474, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="c1258d35-0892-49d9-dd47-93359a6d7ae2"
print(len(pd.unique(uriage_data["item_name"])))

# %% colab={"base_uri": "https://localhost:8080/", "height": 424} id="mNCnoV63AbIz" executionInfo={"status": "ok", "timestamp": 1654454208805, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="84599fde-43ca-4b0d-d232-f812c50732fa"
uriage_data["item_name"] = uriage_data["item_name"].str.upper()
uriage_data["item_name"] = uriage_data["item_name"].str.replace("　", "")
uriage_data["item_name"] = uriage_data["item_name"].str.replace(" ", "")
uriage_data.sort_values(by=["item_name"], ascending=True)

# %% colab={"base_uri": "https://localhost:8080/"} id="OMRJ7Q2pAbI0" executionInfo={"status": "ok", "timestamp": 1654454208806, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="11c6f75d-871f-4801-9cad-7a4dc185de1d"
print(pd.unique(uriage_data["item_name"]))
print(len(pd.unique(uriage_data["item_name"])))

# %% [markdown] id="QvALpZfPAbI1"
# ### ノック１５：金額欠損値の補完をしよう

# %% colab={"base_uri": "https://localhost:8080/"} id="B2GmAaaTAbI1" executionInfo={"status": "ok", "timestamp": 1654454209077, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="21ea2f5d-b2c5-47e5-f0a6-078d8203dfa3"
uriage_data.isnull().any(axis=0)

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="JTuHJmjsAbI1" executionInfo={"status": "ok", "timestamp": 1654454209473, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="881f99b2-1403-4377-8049-ba8e04a4f7a4"
flg_is_null = uriage_data["item_price"].isnull()
for trg in list(uriage_data.loc[flg_is_null, "item_name"].unique()):
    price = uriage_data.loc[(~flg_is_null) & (uriage_data["item_name"] == trg), "item_price"].max()
    uriage_data.loc[(flg_is_null) & (uriage_data["item_name"]==trg),"item_price"] = price
uriage_data.head()

# %% colab={"base_uri": "https://localhost:8080/"} id="997-_YzbAbI2" executionInfo={"status": "ok", "timestamp": 1654454209474, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3ce9ae35-aa81-45c0-c1cd-b8d0a7804045"
uriage_data.isnull().any(axis=0)

# %% colab={"base_uri": "https://localhost:8080/"} id="N_d0kpfuAbI2" executionInfo={"status": "ok", "timestamp": 1654454209841, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="88ae91e6-f9ae-44fe-bb64-d4daa5b4da7c"
for trg in list(uriage_data["item_name"].sort_values().unique()):
    print(trg + "の最大額：" + str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].max()) + "の最小額：" + str(uriage_data.loc[uriage_data["item_name"]==trg]["item_price"].min(skipna=False)))

# %% [markdown] id="4FzUOIHfAbI2"
# ### ノック１６：顧客名の揺れを補正しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="n-JT3pCPAbI3" executionInfo={"status": "ok", "timestamp": 1654454210104, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="69e66a4f-bc90-4976-df40-3c159a199ced"
kokyaku_data["顧客名"].head()

# %% colab={"base_uri": "https://localhost:8080/"} id="C1SylLOOAbI3" executionInfo={"status": "ok", "timestamp": 1654454210457, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="145a6c3d-607a-4269-dcc2-ea9f1644708a"
uriage_data["customer_name"].head()

# %% colab={"base_uri": "https://localhost:8080/"} id="m2MtxaiXAbI3" executionInfo={"status": "ok", "timestamp": 1654454210457, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="60da191d-7ad7-4fcb-a67c-269b6f8e19c9"
kokyaku_data["顧客名"] = kokyaku_data["顧客名"].str.replace("　", "")
kokyaku_data["顧客名"] = kokyaku_data["顧客名"].str.replace(" ", "")
kokyaku_data["顧客名"].head()

# %% [markdown] id="rLINqt9UAbI3"
# ### ノック１７：日付の揺れを補正しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="hWDSGqf2AbI3" executionInfo={"status": "ok", "timestamp": 1654454210817, "user_tz": -540, "elapsed": 1, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="8fcd51fd-1f91-4870-e057-10308f3b86c9"
flg_is_serial = kokyaku_data["登録日"].astype("str").str.isdigit()
flg_is_serial.sum()

# %% colab={"base_uri": "https://localhost:8080/"} id="bFdWuhffAbI4" executionInfo={"status": "ok", "timestamp": 1654454212184, "user_tz": -540, "elapsed": 1029, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a0813264-397c-43f9-f0e6-056656b0e45c"
fromSerial = pd.to_timedelta(kokyaku_data.loc[flg_is_serial, "登録日"].astype("float") - 2, unit="D") + pd.to_datetime('1900/1/1')
fromSerial

# %% colab={"base_uri": "https://localhost:8080/"} id="aGtv-zOjAbI4" executionInfo={"status": "ok", "timestamp": 1654454212185, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="8c874e81-94af-493d-e9ea-062d4062fa73"
fromString = pd.to_datetime(kokyaku_data.loc[~flg_is_serial, "登録日"])
fromString

# %% colab={"base_uri": "https://localhost:8080/", "height": 424} id="yx85YBQwAbI4" executionInfo={"status": "ok", "timestamp": 1654454212185, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0dda05bb-4686-4d03-f1e6-d8d9d02ceadb"
kokyaku_data["登録日"] = pd.concat([fromSerial, fromString])
kokyaku_data

# %% colab={"base_uri": "https://localhost:8080/"} id="lUVQ7Hn5AbI4" executionInfo={"status": "ok", "timestamp": 1654454212541, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="b0d06f89-f94e-4ed0-d885-5510b8d0732b"
kokyaku_data["登録年月"] = kokyaku_data["登録日"].dt.strftime("%Y%m")
rslt = kokyaku_data.groupby("登録年月").count()["顧客名"]
print(rslt)
print(len(kokyaku_data))

# %% colab={"base_uri": "https://localhost:8080/"} id="udZVUNBcAbI4" executionInfo={"status": "ok", "timestamp": 1654454212810, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="41ae975e-4c82-450b-8387-521388cb022b"
flg_is_serial = kokyaku_data["登録日"].astype("str").str.isdigit()
flg_is_serial.sum()

# %% [markdown] id="8VHb8RqWAbI4"
# ### ノック１８：顧客名をキーに２つのデータを結合(ジョイン)しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 659} id="CyU0ijjMAbI4" executionInfo={"status": "ok", "timestamp": 1654454213653, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="33abc032-fa9a-4b79-a028-36f896a77997"
join_data = pd.merge(uriage_data, kokyaku_data, left_on="customer_name", right_on="顧客名", how="left")
join_data = join_data.drop("customer_name", axis=1)
join_data

# %% [markdown] id="m41ZViEfAbI5"
# ### ノック１９：クレンジングしたデータをダンプしよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 424} id="IB3ENIsPAbI5" executionInfo={"status": "ok", "timestamp": 1654454214039, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="8e9a204f-0660-4829-dce3-2036b1d4a973"
dump_data = join_data[["purchase_date", "purchase_month", "item_name", "item_price", "顧客名", "かな", "地域", "メールアドレス", "登録日"]]
dump_data

# %% id="1H_LQgm3AbI5" executionInfo={"status": "ok", "timestamp": 1654454215269, "user_tz": -540, "elapsed": 957, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
dump_data.to_csv("dump_data.csv", index=False)

# %% [markdown] id="BlbjCMdTAbI5"
# ### ノック２０：データを集計しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 659} id="yx55jXOEAbI5" executionInfo={"status": "ok", "timestamp": 1654454215550, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="4d344207-c9d6-4513-9451-233945d94035"
import_data = pd.read_csv("dump_data.csv")
import_data

# %% colab={"base_uri": "https://localhost:8080/", "height": 391} id="p2vpR7NEAbI5" executionInfo={"status": "ok", "timestamp": 1654454216074, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="fe088759-6fe5-4e0a-fb6e-6cd169c21637"
byItem = import_data.pivot_table(index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
byItem

# %% colab={"base_uri": "https://localhost:8080/", "height": 411} id="qCjjo6FbAbI5" executionInfo={"status": "ok", "timestamp": 1654454217294, "user_tz": -540, "elapsed": 516, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="aae5e23b-dc5d-4cd6-baec-24c5ddf10640"
byPrice = import_data.pivot_table(index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
byPrice

# %% colab={"base_uri": "https://localhost:8080/", "height": 408} id="VKiXLihCAbI5" executionInfo={"status": "ok", "timestamp": 1654454217704, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="84c9a6d6-628d-4741-c563-209b5632c770"
byCustomer = import_data.pivot_table(index="purchase_month", columns="顧客名", aggfunc="size", fill_value=0)
byCustomer

# %% colab={"base_uri": "https://localhost:8080/", "height": 300} id="VUf2jATGAbI6" executionInfo={"status": "ok", "timestamp": 1654454218315, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e994d588-a78a-4b42-ffc8-6fbc621ee00a"
byRegion = import_data.pivot_table(index="purchase_month", columns="地域", aggfunc="size", fill_value=0)
byRegion

# %% colab={"base_uri": "https://localhost:8080/", "height": 81} id="S2kjyTyAAbI6" executionInfo={"status": "ok", "timestamp": 1654454218580, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="633da985-41fd-444b-b472-befe91c58641"
away_data = pd.merge(uriage_data, kokyaku_data, left_on="customer_name", right_on="顧客名", how="right")
away_data[away_data["purchase_date"].isnull()][["顧客名", "メールアドレス", "登録日"]]

# %% id="AG4241QLBLWp"
