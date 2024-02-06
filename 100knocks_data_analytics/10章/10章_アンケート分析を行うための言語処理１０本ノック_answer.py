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

# %% colab={"base_uri": "https://localhost:8080/"} id="3uMA8UfV_Xou" executionInfo={"status": "ok", "timestamp": 1654454971740, "user_tz": -540, "elapsed": 19333, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0b715ad8-0bf5-4430-ab56-a3925ef18226"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="AsbbkcTT_bfH" executionInfo={"status": "ok", "timestamp": 1654454971740, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/10章') #ここを変更。

# %% [markdown] id="E5OsyohP_Xox"
# # 10章 アンケート分析を行うための言語処理１０本ノック
#
# ここでは、まちづくりのアンケートを使って分析していきます。  
# 主に言語処理を取り扱っていきます。
# 言語処理特有の処理や、データの持たせ方を学びましょう。

# %% [markdown] id="OqhAmSBl_Xoy"
# ### ノック91：データを読み込んで把握しよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 224} id="PH7rZx3t_Xoz" executionInfo={"status": "ok", "timestamp": 1654454972126, "user_tz": -540, "elapsed": 391, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="f5c35e3d-68a2-442e-e423-82776a932968"
import pandas as pd
survey = pd.read_csv("survey.csv")
print(len(survey))
survey.head()

# %% colab={"base_uri": "https://localhost:8080/"} id="0BsWIJQx_Xo0" executionInfo={"status": "ok", "timestamp": 1654454972127, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0d291800-2a60-4c71-86ff-b5af0e84c54f"
survey.isna().sum()

# %% colab={"base_uri": "https://localhost:8080/"} id="v2U3BnHo_Xo0" executionInfo={"status": "ok", "timestamp": 1654454972128, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5e7aa008-b7d0-4756-c198-e2f7d86847de"
survey = survey.dropna()
survey.isna().sum()

# %% [markdown] id="VpiG40Ti_Xo1"
# ### ノック92：不要な文字を除外してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="qHJl5T3-_Xo1" executionInfo={"status": "ok", "timestamp": 1654454972128, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a9f0a174-f898-4bfb-9bef-9c5f3d0cab6a"
survey["comment"] = survey["comment"].str.replace("AA", "")
survey.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="6xtQ9RbM_Xo1" executionInfo={"status": "ok", "timestamp": 1654454972128, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="6c3c14a5-335f-4145-d7a4-94f638f2992e"
survey["comment"] = survey["comment"].str.replace("\(.+?\)", "", regex=True)
survey.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="AwJBwQgX_Xo2" executionInfo={"status": "ok", "timestamp": 1654454972129, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e605baac-46db-4639-da9d-c17671ecb0ee"
survey["comment"] = survey["comment"].str.replace("\（.+?\）", "", regex=True)
survey.head()

# %% [markdown] id="WPBGz64L_Xo2"
# ### ノック93：文字数をカウントしてヒストグラムを表示してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="i6Pqa73D_Xo3" executionInfo={"status": "ok", "timestamp": 1654454972129, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="9b421288-3804-4e5f-d1af-2f15c7ca0819"
survey["length"] = survey["comment"].str.len()
survey.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 322} id="4RnUVGgU_Xo3" executionInfo={"status": "ok", "timestamp": 1654454972572, "user_tz": -540, "elapsed": 453, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="b02190fa-e31d-43d3-d9a2-0c9b9438a4b9"
import matplotlib.pyplot as plt
# %matplotlib inline
plt.hist(survey["length"])

# %% [markdown] id="p30DUp5P_Xo3"
# ### ノック94：形態素解析で文章を分割してみよう

# %% id="M4qbvyE3_y2r" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1654454997189, "user_tz": -540, "elapsed": 24621, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="b8c6cef3-5cab-443a-a809-45716224156a"
# !pip install mecab-python3 unidic-lite

# %% colab={"base_uri": "https://localhost:8080/", "height": 72} id="HkMFvf7c_Xo3" executionInfo={"status": "ok", "timestamp": 1654454997189, "user_tz": -540, "elapsed": 18, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="4c42bb2c-1cc3-4d24-c315-f81346e9d80d"
import MeCab
tagger = MeCab.Tagger()
text = "すもももももももものうち"
words = tagger.parse(text)
words

# %% colab={"base_uri": "https://localhost:8080/"} id="mJKjLazK_Xo4" executionInfo={"status": "ok", "timestamp": 1654454997190, "user_tz": -540, "elapsed": 18, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a8e9f16c-eda7-4717-c9fb-82f6feb22f5c"
words = tagger.parse(text).splitlines()
words_arr = []
for i in words:
    if i == 'EOS': continue
    word_tmp = i.split()[0]
    words_arr.append(word_tmp)
words_arr

# %% [markdown] id="Cf7gIxT8_Xo4"
# ### ノック95：形態素解析で文章から「動詞・名詞」を抽出してみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="Gx-DY3EJ_Xo4" executionInfo={"status": "ok", "timestamp": 1654454997190, "user_tz": -540, "elapsed": 16, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e9e98bec-2322-4784-ddf9-de3874ca0858"
text = "すもももももももものうち"
words = tagger.parse(text).splitlines()
words_arr = []
parts = ["名詞", "動詞"]
for i in words:
    if i == 'EOS' or i == '': continue
    word_tmp = i.split()[0]
    part = i.split()[4].split("-")[0]
    if not (part in parts):continue
    words_arr.append(word_tmp)
words_arr

# %% [markdown] id="1N-gwIRL_Xo4"
# ### ノック96：形態素解析で抽出した頻出する名詞を確認してみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="zEaXSzUh_Xo4" executionInfo={"status": "ok", "timestamp": 1654454997190, "user_tz": -540, "elapsed": 14, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="b801e7ca-5c82-4e7e-a5f2-3970f3ce6c22"
all_words = []
parts = ["名詞"]
for n in range(len(survey)):
    text = survey["comment"].iloc[n]
    words = tagger.parse(text).splitlines()
    words_arr = []
    for i in words:
        if i == "EOS" or i == "": continue
        word_tmp = i.split()[0]
        if len(i.split())>=4:
            part = i.split()[4].split("-")[0]
            if not (part in parts):continue
            words_arr.append(word_tmp)
    all_words.extend(words_arr)
print(all_words)

# %% colab={"base_uri": "https://localhost:8080/", "height": 708} id="nwYhsyEE_Xo5" executionInfo={"status": "ok", "timestamp": 1654454997190, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e6d9cb06-1afd-4f36-8b7f-98f00cda699e"
all_words_df = pd.DataFrame({"words":all_words, "count":len(all_words)*[1]})
all_words_df = all_words_df.groupby("words").sum()
all_words_df.sort_values("count",ascending=False).head(20)

# %% [markdown] id="Q4B4uSBh_Xo5"
# ### ノック97：関係のない単語を除去しよう

# %% colab={"base_uri": "https://localhost:8080/"} id="-viLw6aY_Xo5" executionInfo={"status": "ok", "timestamp": 1654454997190, "user_tz": -540, "elapsed": 13, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="2a53aabb-b295-45f2-bbdf-35e7cd7ef4d5"
stop_words = ["時"]
all_words = []
parts = ["名詞"]
for n in range(len(survey)):
    text = survey["comment"].iloc[n]
    words = tagger.parse(text).splitlines()
    words_arr = []
    for i in words:
        if i == "EOS" or i == "": continue
        word_tmp = i.split()[0]
        if len(i.split())>=4:
            part = i.split()[4].split("-")[0]
            if not (part in parts):continue
            if word_tmp in stop_words:continue
            words_arr.append(word_tmp)
    all_words.extend(words_arr)
print(all_words)

# %% colab={"base_uri": "https://localhost:8080/", "height": 708} id="VMWYUQ9T_Xo5" executionInfo={"status": "ok", "timestamp": 1654454997191, "user_tz": -540, "elapsed": 12, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="1ae47227-0a95-4eb6-def9-06e952d8ab60"
all_words_df = pd.DataFrame({"words":all_words, "count":len(all_words)*[1]})
all_words_df = all_words_df.groupby("words").sum()
all_words_df.sort_values("count",ascending=False).head(20)

# %% [markdown] id="U78BVUsV_Xo5"
# ### ノック98：顧客満足度と頻出単語の関係をみてみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="tnz_8Lgu_Xo6" executionInfo={"status": "ok", "timestamp": 1654454997191, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5591f889-ce8c-437a-d4d9-e5738e594fc0"
stop_words = ["時"]
parts = ["名詞"]
all_words = []
satisfaction = []
for n in range(len(survey)):
    text = survey["comment"].iloc[n]
    words = tagger.parse(text).splitlines()
    words_arr = []
    for i in words:
        if i == "EOS" or i == "": continue
        word_tmp = i.split()[0]
        if len(i.split())>=4:
            part = i.split()[4].split("-")[0]
            if not (part in parts):continue
            if word_tmp in stop_words:continue
            words_arr.append(word_tmp)
            satisfaction.append(survey["satisfaction"].iloc[n])
    all_words.extend(words_arr)
all_words_df = pd.DataFrame({"words":all_words, "satisfaction":satisfaction, "count":len(all_words)*[1]})
all_words_df.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 237} id="m8LfCYd9_Xo6" executionInfo={"status": "ok", "timestamp": 1654454997191, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="91ba9a44-1ba9-43ee-8328-ee41ab55b3fb"
words_satisfaction = all_words_df.groupby("words").mean()["satisfaction"]
words_count = all_words_df.groupby("words").sum()["count"]
words_df = pd.concat([words_satisfaction, words_count], axis=1)
words_df.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 237} id="c9VFlfX-_Xo6" executionInfo={"status": "ok", "timestamp": 1654454997542, "user_tz": -540, "elapsed": 361, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="cd40245f-be90-4fb9-f74e-6c708a60e088"
words_df = words_df.loc[words_df["count"]>=3]
words_df.sort_values("satisfaction", ascending=False).head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 237} id="gSS_4RkU_Xo6" executionInfo={"status": "ok", "timestamp": 1654454997543, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="eea694c9-60e5-455c-e0a3-2c2b3da21f21"
words_df.sort_values("satisfaction").head()

# %% [markdown] id="V29e9Qxw_Xo6"
# ### ノック99：アンケート毎の特徴を表現してみよう

# %% colab={"base_uri": "https://localhost:8080/", "height": 235} id="vvYSQESs_Xo6" executionInfo={"status": "ok", "timestamp": 1654454997890, "user_tz": -540, "elapsed": 351, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="0d578686-0e8b-4016-a7f8-cf677d7d40e9"
parts = ["名詞"]
all_words_df = pd.DataFrame()
satisfaction = []
for n in range(len(survey)):
    text = survey["comment"].iloc[n]
    words = tagger.parse(text).splitlines()
    words_df = pd.DataFrame()
    for i in words:
        if i == "EOS" or i == "": continue
        word_tmp = i.split()[0]
        if len(i.split())>=4:
            part = i.split()[4].split("-")[0]
            if not (part in parts):continue
            words_df[word_tmp] = [1]
    all_words_df = pd.concat([all_words_df, words_df] ,ignore_index=True)
all_words_df.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 235} id="mtkupxLj_Xo6" executionInfo={"status": "ok", "timestamp": 1654454998268, "user_tz": -540, "elapsed": 382, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="42132045-6546-4e96-fa29-92f64ef45ffe"
all_words_df = all_words_df.fillna(0)
all_words_df.head()

# %% [markdown] id="b-szMUmz_Xo7"
# ### ノック100：類似アンケートを探してみよう

# %% colab={"base_uri": "https://localhost:8080/"} id="km5FXlga_Xo7" executionInfo={"status": "ok", "timestamp": 1654454998268, "user_tz": -540, "elapsed": 8, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="c07f406e-5fb5-4d65-caef-fd454aeb2ef6"
print(survey["comment"].iloc[2])
target_text = all_words_df.iloc[2]
print(target_text)

# %% colab={"base_uri": "https://localhost:8080/", "height": 279} id="HwuIVOs7_Xo7" executionInfo={"status": "ok", "timestamp": 1654454998268, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="86994f6f-a520-4cb4-a2e5-9c8b65012932"
import numpy as np
cos_sim = []
for i in range(len(all_words_df)):
    cos_text = all_words_df.iloc[i]
    cos = np.dot(target_text, cos_text) / (np.linalg.norm(target_text) * np.linalg.norm(cos_text))
    cos_sim.append(cos)
all_words_df["cos_sim"] = cos_sim
all_words_df.sort_values("cos_sim",ascending=False).head()

# %% colab={"base_uri": "https://localhost:8080/"} id="nkkBKkl__Xo7" executionInfo={"status": "ok", "timestamp": 1654454998632, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="82405881-4d5a-481b-a4ba-fa6269e383f8"
print(survey["comment"].iloc[2])
print(survey["comment"].iloc[24])
print(survey["comment"].iloc[15])
print(survey["comment"].iloc[33])

# %% id="Dkv79sSbCwx-"
