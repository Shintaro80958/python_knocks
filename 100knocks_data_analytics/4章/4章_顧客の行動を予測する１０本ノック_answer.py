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

# %% colab={"base_uri": "https://localhost:8080/"} id="dKYhhdaMEKIT" executionInfo={"status": "ok", "timestamp": 1654454405353, "user_tz": -540, "elapsed": 28332, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="f57f3e9c-634a-4f90-8550-0a39e4a2b8eb"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="b39yFDKQEOM8" executionInfo={"status": "ok", "timestamp": 1654454405354, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/4章') #ここを変更。

# %% [markdown] id="o-XZJTbpEKIX"
# # 4章 顧客の全体像を把握する１０本ノック
#
# 引き続き、スポーツジムの会員データを使って顧客の行動を分析していきます。  
# ３章で顧客の全体像を把握しました。  
# ここからは、機械学習を用いて顧客のグループ化や顧客の利用予測行なっていきましょう。  
# ここでは、教師なし学習、教師あり学習の回帰を取り扱います。

# %% [markdown] id="h8vmeAx0EKIY"
# ### ノック31：データを読み込んで確認しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="B6gqzrsHEKIZ" executionInfo={"status": "ok", "timestamp": 1654454407831, "user_tz": -540, "elapsed": 2480, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="03f99a6b-7a74-4af0-bf3f-c0099c02464d"
import pandas as pd
uselog = pd.read_csv('use_log.csv')
uselog.isnull().sum()

# %% colab={"base_uri": "https://localhost:8080/"} id="Mdszw5UaEKIa" executionInfo={"status": "ok", "timestamp": 1654454408350, "user_tz": -540, "elapsed": 523, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="65bcb737-2807-456a-c800-3d6d976af053"
customer = pd.read_csv('customer_join.csv')
customer.isnull().sum()

# %% [markdown] id="-PsQzN1XEKIa"
# ### ノック32：クラスタリングで顧客をグループ化しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="8KUgMYH9EKIa" executionInfo={"status": "ok", "timestamp": 1654454408350, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e9483d7c-ed83-4877-da9a-bca4c8dc3952"
customer_clustering = customer[["mean", "median","max", "min", "membership_period"]]
customer_clustering.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 224} id="KtP6w_NrEKIb" executionInfo={"status": "ok", "timestamp": 1654454409329, "user_tz": -540, "elapsed": 982, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="36a0d3b6-3cf5-40ff-8053-b22ccef1d0f0"
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)

kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering = customer_clustering.assign(cluster = clusters.labels_)

print(customer_clustering["cluster"].unique())
customer_clustering.head()

# %% [markdown] id="-doDBMHyEKIb"
# ### ノック33：クラスタリング結果を分析しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="6sQTeb74EKIc" executionInfo={"status": "ok", "timestamp": 1654454409330, "user_tz": -540, "elapsed": 9, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="dca1b82a-9be7-4798-89b2-68d1375f5795"
customer_clustering.columns = ["月内平均値","月内中央値", "月内最大値", "月内最小値","会員期間", "cluster"]
customer_clustering.groupby("cluster").count()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="NbJal6SyEKIc" executionInfo={"status": "ok", "timestamp": 1654454409330, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="17ad59f6-3b6c-4c5c-96b7-20053d29f325"
customer_clustering.groupby("cluster").mean()

# %% [markdown] id="VZKRKfThEKId"
# ### ノック34：クラスタリング結果を可視化してみよう

# %% id="irBl3jUCEKId" executionInfo={"status": "ok", "timestamp": 1654454410009, "user_tz": -540, "elapsed": 684, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
from sklearn.decomposition import PCA
X = customer_clustering_sc
pca = PCA(n_components=2)
pca.fit(X)
x_pca = pca.transform(X)
pca_df = pd.DataFrame(x_pca)
pca_df["cluster"] = customer_clustering["cluster"]

# %% colab={"base_uri": "https://localhost:8080/", "height": 265} id="vvCGwoYLEKId" executionInfo={"status": "ok", "timestamp": 1654454410010, "user_tz": -540, "elapsed": 14, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0a9def7c-40d9-4b60-e2e0-9b8553c3ce7e"
import matplotlib.pyplot as plt
# %matplotlib inline
for i in customer_clustering["cluster"].unique():
    tmp = pca_df.loc[pca_df["cluster"]==i]
    plt.scatter(tmp[0], tmp[1])

# %% [markdown] id="7xxtlpFlEKIe"
# ### ノック35：クラスタリング結果をもとに退会顧客の傾向を把握しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 269} id="-fT0K2epEKIe" executionInfo={"status": "ok", "timestamp": 1654454410010, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="d8a3c96b-5f6d-45b9-a5f6-4aa80175e630"
customer_clustering = pd.concat([customer_clustering, customer], axis=1)
customer_clustering.groupby(["cluster","is_deleted"],as_index=False).count()[["cluster","is_deleted","customer_id"]]

# %% colab={"base_uri": "https://localhost:8080/", "height": 300} id="dugcfhGQEKIe" executionInfo={"status": "ok", "timestamp": 1654454410011, "user_tz": -540, "elapsed": 9, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="28189e88-5422-46f7-b16d-e19c1744196f"
customer_clustering.groupby(["cluster","routine_flg"],as_index=False).count()[["cluster","routine_flg","customer_id"]]

# %% [markdown] id="GfhcjnwJEKIf"
# ### ノック36：翌月の利用回数予測を行うためのデータ準備をしよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="emVyJtgiEKIf" executionInfo={"status": "ok", "timestamp": 1654454411925, "user_tz": -540, "elapsed": 1922, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="4ebe9b23-7c95-43a9-ba44-f5e65afaf701"
uselog["usedate"] = pd.to_datetime(uselog["usedate"])
uselog["年月"] = uselog["usedate"].dt.strftime("%Y%m")
uselog_months = uselog.groupby(["年月","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]
uselog_months.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="MrQtiE9EEKIf" executionInfo={"status": "ok", "timestamp": 1654454411926, "user_tz": -540, "elapsed": 16, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="8f21f5c9-2b17-4b09-c829-eab9cca32158"
year_months = list(uselog_months["年月"].unique())
predict_data = pd.DataFrame()
for i in range(6, len(year_months)):
    tmp = uselog_months.loc[uselog_months["年月"]==year_months[i]].copy()
    tmp.rename(columns={"count":"count_pred"}, inplace=True)
    for j in range(1, 7):
        tmp_before = uselog_months.loc[uselog_months["年月"]==year_months[i-j]].copy()
        del tmp_before["年月"]
        tmp_before.rename(columns={"count":"count_{}".format(j-1)}, inplace=True)
        tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
    predict_data = pd.concat([predict_data, tmp], ignore_index=True)
predict_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="sl8utsCYEKIf" executionInfo={"status": "ok", "timestamp": 1654454411927, "user_tz": -540, "elapsed": 14, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="bf0cd72e-fccc-43e1-9377-dbe8eb46ffaa"
predict_data = predict_data.dropna()
predict_data = predict_data.reset_index(drop=True)
predict_data.head()

# %% [markdown] id="2xqmKtu_EKIg"
# ### ノック37：特徴となる変数を付与しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="pu9KvVY_EKIg" executionInfo={"status": "ok", "timestamp": 1654454411928, "user_tz": -540, "elapsed": 14, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="53adde6d-5273-4610-8c08-0c5f3512d2d0"
predict_data = pd.merge(predict_data, customer[["customer_id","start_date"]], on="customer_id", how="left")
predict_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="uDA_U22FEKIg" executionInfo={"status": "ok", "timestamp": 1654454422650, "user_tz": -540, "elapsed": 10734, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="58407148-da6d-4d37-daa8-dd7be75b8a30"
predict_data["now_date"] = pd.to_datetime(predict_data["年月"], format="%Y%m")
predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
from dateutil.relativedelta import relativedelta
predict_data["period"] = None
for i in range(len(predict_data)):
    delta = relativedelta(predict_data.loc[i,"now_date"], predict_data.loc[i,"start_date"])
    predict_data.loc[i,"period"] = delta.years*12 + delta.months
predict_data.head()

# %% [markdown] id="M2_fsqeTEKIg"
# ### ノック38：来月の利用回数予測モデルを作成しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="e7Q52enEEKIg" executionInfo={"status": "ok", "timestamp": 1654454422650, "user_tz": -540, "elapsed": 17, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="828104ce-6608-453f-e8c9-1397f62d6b4d"
predict_data = predict_data.loc[predict_data["start_date"]>=pd.to_datetime("20180401")]
from sklearn import linear_model
import sklearn.model_selection
model = linear_model.LinearRegression()
X = predict_data[["count_0","count_1","count_2","count_3","count_4","count_5","period"]]
y = predict_data["count_pred"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, random_state=0)
model.fit(X_train, y_train)

# %% colab={"base_uri": "https://localhost:8080/"} id="oRLw3FRlEKIh" executionInfo={"status": "ok", "timestamp": 1654454422651, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="91203b1f-0093-4ab5-db74-d0d382cf13d0"
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

# %% [markdown] id="IJ6SOnajEKIh"
# ### ノック39：モデルに寄与している変数を確認しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 269} id="WKQIy7uxEKIh" executionInfo={"status": "ok", "timestamp": 1654454422651, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="04bb2937-9951-4da6-d37f-11ec25c5388f"
coef = pd.DataFrame({"feature_names":X.columns, "coefficient":model.coef_})
coef

# %% [markdown] id="Va5ovC5yEKIh"
# ### ノック40：来月の利用回数を予測しよう

# %% id="gC5E_cOAEKIh" executionInfo={"status": "ok", "timestamp": 1654454422651, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
x1 = [3, 4, 4, 6, 8, 7, 8]
x2 = [2, 2, 3, 3, 4, 6, 8]
x_pred = pd.DataFrame(data=[x1, x2],columns=["count_0","count_1","count_2","count_3","count_4","count_5","period"])

# %% colab={"base_uri": "https://localhost:8080/"} id="Zz-ZePj8EKIh" executionInfo={"status": "ok", "timestamp": 1654454422652, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a6a90054-4fac-4545-e449-04b34265f7e4"
model.predict(x_pred)

# %% id="CeQqkfbmEKIh" executionInfo={"status": "ok", "timestamp": 1654454423167, "user_tz": -540, "elapsed": 521, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
uselog_months.to_csv("use_log_months.csv",index=False)

# %% id="HMtDzYrkP6Y5"
