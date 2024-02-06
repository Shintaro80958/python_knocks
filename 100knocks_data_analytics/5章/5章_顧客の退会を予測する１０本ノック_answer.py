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

# %% colab={"base_uri": "https://localhost:8080/"} id="mI6kndokQcNK" executionInfo={"status": "ok", "timestamp": 1654454498767, "user_tz": -540, "elapsed": 24261, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5f2dda39-a3f1-4914-faf3-e5913aa4cd8c"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="UQ_6SKw3Qex0" executionInfo={"status": "ok", "timestamp": 1654454499136, "user_tz": -540, "elapsed": 373, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/5章') #ここを変更。

# %% [markdown] id="6Ao35733QcNO"
# # 5章 顧客の退会を予測する１０本ノック
#
# 引き続き、スポーツジムの会員データを使って顧客の行動を分析していきます。  
# ３章では顧客の全体像を把握し、4章では数ヶ月利用している顧客の来月の利用回数の予測を行いました。   
# ここでは、教師あり学習の分類を用いて、顧客の退会予測を取り扱います。

# %% [markdown] id="uJrG-JVwQcNQ"
# ### ノック41：データを読み込んで利用データを整形しよう

# %% id="AyuBQUvgQcNR" executionInfo={"status": "ok", "timestamp": 1654454502036, "user_tz": -540, "elapsed": 1281, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
import pandas as pd
customer = pd.read_csv('customer_join.csv')
uselog_months = pd.read_csv('use_log_months.csv')

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="7-ocPeZpQcNR" executionInfo={"status": "ok", "timestamp": 1654454502448, "user_tz": -540, "elapsed": 414, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="42e9017d-ad69-4215-a129-2af96d4c663e"
year_months = list(uselog_months["年月"].unique())
uselog = pd.DataFrame()
for i in range(1, len(year_months)):
    tmp = uselog_months.loc[uselog_months["年月"]==year_months[i]].copy()
    tmp.rename(columns={"count":"count_0"}, inplace=True)
    tmp_before = uselog_months.loc[uselog_months["年月"]==year_months[i-1]].copy()
    del tmp_before["年月"]
    tmp_before.rename(columns={"count":"count_1"}, inplace=True)
    tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
    uselog = pd.concat([uselog, tmp], ignore_index=True)
uselog.head()

# %% [markdown] id="vFuasxjDQcNS"
# ### ノック42：退会前月の退会顧客データを作成しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 318} id="Qdv0ExJPQcNT" executionInfo={"status": "ok", "timestamp": 1654454503193, "user_tz": -540, "elapsed": 748, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e1d450be-f9b0-41de-e52f-6cb4187d1751"
from dateutil.relativedelta import relativedelta
exit_customer = customer.loc[customer["is_deleted"]==1].copy()
exit_customer["exit_date"] = None
exit_customer["end_date"] = pd.to_datetime(exit_customer["end_date"])
for i in exit_customer.index:
    exit_customer.loc[i,"exit_date"] = exit_customer.loc[i,"end_date"] - relativedelta(months=1)
exit_customer["exit_date"] = pd.to_datetime(exit_customer["exit_date"])
exit_customer["年月"] = exit_customer["exit_date"].dt.strftime("%Y%m")
uselog["年月"] = uselog["年月"].astype(str)
exit_uselog = pd.merge(uselog, exit_customer, on=["customer_id", "年月"], how="left")
print(len(uselog))
exit_uselog.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 422} id="PyecryRoQcNT" executionInfo={"status": "ok", "timestamp": 1654454503194, "user_tz": -540, "elapsed": 9, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="b2fd5190-6d3b-478e-8b95-3d3e92b8b093"
exit_uselog = exit_uselog.dropna(subset=["name"])
print(len(exit_uselog))
print(len(exit_uselog["customer_id"].unique()))
exit_uselog.head()

# %% [markdown] id="dpJGYHVSQcNU"
# ### ノック43：継続顧客のデータを作成しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="lZskwmcQQcNU" executionInfo={"status": "ok", "timestamp": 1654454503556, "user_tz": -540, "elapsed": 369, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="543ab2c2-234d-47c7-bece-29d60fabcac5"
conti_customer = customer.loc[customer["is_deleted"]==0]
conti_uselog = pd.merge(uselog, conti_customer, on=["customer_id"], how="left")
print(len(conti_uselog))
conti_uselog = conti_uselog.dropna(subset=["name"])
print(len(conti_uselog))

# %% colab={"base_uri": "https://localhost:8080/", "height": 404} id="DhzoYbtTQcNU" executionInfo={"status": "ok", "timestamp": 1654454503557, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="8cbdbebf-a2ef-4c32-962f-0fc150a35d88"
conti_uselog = conti_uselog.sample(frac=1, random_state=0).reset_index(drop=True)
conti_uselog = conti_uselog.drop_duplicates(subset="customer_id")
print(len(conti_uselog))
conti_uselog.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 404} id="rQFdgVasQcNV" executionInfo={"status": "ok", "timestamp": 1654454503557, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="555cff2e-f57d-46eb-c80b-53dea533807f"
predict_data = pd.concat([conti_uselog, exit_uselog],ignore_index=True)
print(len(predict_data))
predict_data.head()

# %% [markdown] id="5AhrGbMNQcNV"
# ### ノック44：予測する月の在籍期間を作成しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 386} id="2xb7EhrgQcNV" executionInfo={"status": "ok", "timestamp": 1654454505558, "user_tz": -540, "elapsed": 2006, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="9d3a8d50-3a16-46ad-8439-ef1330539dd2"
predict_data["period"] = 0
predict_data["now_date"] = pd.to_datetime(predict_data["年月"], format="%Y%m")
predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
for i in range(len(predict_data)):
    delta = relativedelta(predict_data.loc[i, "now_date"], predict_data.loc[i, "start_date"])
    predict_data.loc[i, "period"] = int(delta.years*12 + delta.months)
predict_data.head()

# %% [markdown] id="riisq7kfQcNW"
# ### ノック45：欠損値を除去しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="xpwMzXIMQcNW" executionInfo={"status": "ok", "timestamp": 1654454505558, "user_tz": -540, "elapsed": 15, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="7b46da48-871a-43ff-da82-91e2112c8787"
predict_data.isna().sum()

# %% colab={"base_uri": "https://localhost:8080/"} id="xwOqIN_8QcNW" executionInfo={"status": "ok", "timestamp": 1654454505559, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="51931e48-e1a6-42d5-d67d-edd08b69c089"
predict_data = predict_data.dropna(subset=["count_1"])
predict_data.isna().sum()

# %% [markdown] id="IXA8hJQMQcNW"
# ### ノック46：文字列型の変数を処理できるように整形しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="TLdP2l0jQcNW" executionInfo={"status": "ok", "timestamp": 1654454505559, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0771016d-e061-4090-d934-4f6e86cffb11"
target_col = ["campaign_name", "class_name", "gender", "count_1", "routine_flg", "period", "is_deleted"]
predict_data = predict_data[target_col]
predict_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 305} id="fy0RAiRMQcNX" executionInfo={"status": "ok", "timestamp": 1654454505559, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="762229ee-025a-4585-e7f5-9d828670242a"
predict_data = pd.get_dummies(predict_data)
predict_data.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 267} id="azmbAyTVQcNX" executionInfo={"status": "ok", "timestamp": 1654454505560, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="f42f2c08-dbdf-4788-fe45-4f7b5dbf0bb2"
del predict_data["campaign_name_通常"]
del predict_data["class_name_ナイト"]
del predict_data["gender_M"]
predict_data.head()

# %% [markdown] id="WjyB5ZoXQcNX"
# ### ノック47：決定木を用いて退会予測モデルを作成してみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="41_d77_4QcNX" executionInfo={"status": "ok", "timestamp": 1654454506173, "user_tz": -540, "elapsed": 622, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="9bc00740-bff0-41bb-d553-4b0a2cb31f9a"
from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection

exit = predict_data.loc[predict_data["is_deleted"]==1]
conti = predict_data.loc[predict_data["is_deleted"]==0].sample(len(exit), random_state=0)

X = pd.concat([exit, conti], ignore_index=True)
y = X["is_deleted"]
del X["is_deleted"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, random_state=0)

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)
y_test_pred = model.predict(X_test)
print(y_test_pred)

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="5BGjLL4VQcNY" executionInfo={"status": "ok", "timestamp": 1654454506630, "user_tz": -540, "elapsed": 459, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="92187e89-c317-4a6c-e99b-71bc09351e1d"
results_test = pd.DataFrame({"y_test":y_test ,"y_pred":y_test_pred })
results_test.head()

# %% [markdown] id="vtMsAyaqQcNY"
# ### ノック48：予測モデルの評価を行ない、モデルのチューニングをしてみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="xYYAsdd8QcNY" executionInfo={"status": "ok", "timestamp": 1654454506631, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="03faea2b-bbcd-4632-d9c1-66e7c9065a58"
correct = len(results_test.loc[results_test["y_test"]==results_test["y_pred"]])
data_count = len(results_test)
score_test = correct / data_count
print(score_test)

# %% colab={"base_uri": "https://localhost:8080/"} id="ti5Ua_zcQcNY" executionInfo={"status": "ok", "timestamp": 1654454506631, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="1827b34e-3c5d-494c-b9d4-7ec6e3abec70"
print(model.score(X_test, y_test))
print(model.score(X_train, y_train))

# %% colab={"base_uri": "https://localhost:8080/"} id="tExk6S0xQcNY" executionInfo={"status": "ok", "timestamp": 1654454506631, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e25477f3-ddfb-4c5c-875c-bae345197513"
X = pd.concat([exit, conti], ignore_index=True)
y = X["is_deleted"]
del X["is_deleted"]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, random_state=0)

model = DecisionTreeClassifier(random_state=0, max_depth=5)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(model.score(X_train, y_train))

# %% [markdown] id="ZMykXKF_QcNY"
# ### ノック49：モデルに寄与している変数を確認しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 300} id="UzhacET4QcNY" executionInfo={"status": "ok", "timestamp": 1654454506631, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="2fb3ff56-4ccd-43ad-8aca-44a7ef1a03af"
importance = pd.DataFrame({"feature_names":X.columns, "coefficient":model.feature_importances_})
importance

# %% id="ic4J74EvT9GZ" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1654454513931, "user_tz": -540, "elapsed": 7305, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="90a85a21-e94a-4cf8-8782-1a9d84edb118"
# !pip install japanize_matplotlib
from sklearn import tree
import matplotlib.pyplot as plt
import japanize_matplotlib
# %matplotlib inline

plt.figure(figsize=(20,8))
tree.plot_tree(model,feature_names=X.columns,fontsize=8)

# %% [markdown] id="ZwHkKtJfQcNY"
# ### ノック50：顧客の退会を予測しよう

# %% id="pyFlfJ7xQcNY" executionInfo={"status": "ok", "timestamp": 1654454514178, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
count_1 = 3
routine_flg = 1
period = 10
campaign_name = "入会費無料"
class_name = "オールタイム"
gender = "M"

# %% id="l9aVdUSQQcNZ" executionInfo={"status": "ok", "timestamp": 1654454514179, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
if campaign_name == "入会費半額":
    campaign_name_list = [1, 0]
elif campaign_name == "入会費無料":
    campaign_name_list = [0, 1]
elif campaign_name == "通常":
    campaign_name_list = [0, 0]
if class_name == "オールタイム":
    class_name_list = [1, 0]
elif class_name == "デイタイム":
    class_name_list = [0, 1]
elif class_name == "ナイト":
    class_name_list = [0, 0]
if gender == "F":
    gender_list = [1]
elif gender == "M":
    gender_list = [0]
input_data = [count_1, routine_flg, period]
input_data.extend(campaign_name_list)
input_data.extend(class_name_list)
input_data.extend(gender_list)
input_data = pd.DataFrame(data=[input_data], columns=X.columns)

# %% colab={"base_uri": "https://localhost:8080/"} id="5mNFKsyvQcNZ" executionInfo={"status": "ok", "timestamp": 1654454514179, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="c122e827-503b-478b-b53e-ddad1c01ffc8"
print(model.predict(input_data))
print(model.predict_proba(input_data))

# %% id="WEDI2SEVQcNZ"
