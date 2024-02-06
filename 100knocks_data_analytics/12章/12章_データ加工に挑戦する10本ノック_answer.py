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

# %% id="CQhZLbtQAeEI" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1654455149710, "user_tz": -540, "elapsed": 19128, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="5e31bbab-3742-4e01-d522-23e825fd99f6"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="vF_JshRtAfOp" executionInfo={"status": "ok", "timestamp": 1654455149710, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/12章') #ここを変更。

# %% [markdown] id="9H1wpviFAbIq"
# # １２章　データ加工に挑戦する１０本ノック
#
# 本章ではデータ加工を扱う10個の課題に挑戦してみましょう。
#
# 放課後ノックということで、本編のようなストーリー仕立てではなく入力データと出力データを定義した後は、各自フリーにプログラムでデータ加工を行ってみて下さい。
#
# 解答の一例としてサンプルソースを用意していますが、ここまでノックを行ってきた皆様なら、PythonやPandasなどの取り扱いにも十分慣れてきていると思いますので、出来る限り色々ご自身で調べたり、試行錯誤したりしながらトライしてみてください。
#

# %% [markdown] id="JY-0mpyyAbIt"
# ### 放課後ノック１１１：”よくある”エクセルデータに挑戦

# %% id="BVYPHVH3xAsa" executionInfo={"status": "ok", "timestamp": 1654455156465, "user_tz": -540, "elapsed": 590, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
import pandas as pd

# %% id="qi6XXxsyAbIu" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1654455157512, "user_tz": -540, "elapsed": 1049, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="800d6d32-01ff-4f0c-e4bf-1a2d358e994d"
# エクセルファイルの読み込み
input_data = pd.read_excel("12-1.xlsx")
input_data.head()

# %% id="0NfqK54_AbIv" colab={"base_uri": "https://localhost:8080/", "height": 175} executionInfo={"status": "ok", "timestamp": 1654455157513, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="6b273615-d49a-4163-a496-dcc0fa2041c4"
# 人数項目を男女それぞれに横に持たせてデータを整理する
men = input_data['人数（男性、女性）'][0::2]
women = input_data['人数（男性、女性）'][1::2]

men.reset_index(inplace=True, drop=True)
women.reset_index(inplace=True, drop=True)

output_data = input_data[0::2].copy()
output_data.reset_index(inplace=True, drop=True)
output_data['男性'] = men
output_data['女性'] = women

# 不要となったカラム「人数（男性、女性）」を削除
output_data.drop('人数（男性、女性）', axis=1, inplace=True)

# 欠損している都道府県を設定
output_data.iat[1, 0] = output_data.iat[0, 0]
output_data.iat[3, 0] = output_data.iat[2, 0]

output_data.head()

# %% id="AL-wmJscwavr" executionInfo={"status": "ok", "timestamp": 1654455157513, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvファイルに出力
output_data.to_csv('12-1_out.csv', index=False)

# %% [markdown] id="-kiPZP1AAbIv"
# ### 放課後ノック１１２： エクセルの社員マスタ加工に挑戦

# %% id="YpYFUtvFAbIw" colab={"base_uri": "https://localhost:8080/", "height": 332} executionInfo={"status": "ok", "timestamp": 1654455157877, "user_tz": -540, "elapsed": 368, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="cb24e7c5-f8b3-4059-baef-ac1c95649f06"
# エクセルファイルの読み込み
input_data = pd.read_excel("12-2.xlsx")
input_data

# %% id="wrzVsWI3AbIw" colab={"base_uri": "https://localhost:8080/", "height": 237} executionInfo={"status": "ok", "timestamp": 1654455157877, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="c72650e8-ad06-4e6b-c035-8245175741cb"
# 役職のNaNを空文字に
output_data = input_data.copy()
output_data['役職'].fillna('', inplace=True)

# データを更新日で並び替え
output_data.sort_values('更新日', ascending=True, inplace=True)

# 重複するデータを特定し、新しいデータを保持
output_data.drop_duplicates(subset=['社員名', '生年月日'], keep='last', inplace=True)

output_data

# %% id="5-eR9XYZ-5Af" executionInfo={"status": "ok", "timestamp": 1654455157878, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvファイルに出力
output_data.to_csv('12-2_out.csv', index=False)

# %% [markdown] id="6j4JAl_uAbIx"
# ### 放課後ノック１１３： 正規化に挑戦

# %% id="N5pLAkwZAbIy" colab={"base_uri": "https://localhost:8080/", "height": 175} executionInfo={"status": "ok", "timestamp": 1654455158463, "user_tz": -540, "elapsed": 289, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e0afc3b2-45ac-4ace-cc49-224e019e904f"
# エクセルファイルの読み込み
input_data = pd.read_excel("12-3.xlsx")
input_data

# %% id="d4MEUWc8AbIy" colab={"base_uri": "https://localhost:8080/", "height": 175} executionInfo={"status": "ok", "timestamp": 1654455158812, "user_tz": -540, "elapsed": 352, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="fc9fe058-289b-4565-8484-781956ee1d3f"
# セル結合の欠損値を埋める（今回はA農家のみ欠損なのでfillnaを用いる事が可能）
input_data['仕入先'].fillna(input_data['仕入先'][0], inplace=True)
input_data['仕入先TEL'].fillna(input_data['仕入先TEL'][0], inplace=True)

# 仕入先を別のデータフレームに格納
farmer_data = input_data[['仕入先', '仕入先TEL']].copy()
farmer_data.drop_duplicates(inplace=True)

# 仕入先のキーを生成
farmer_idx = []
idx = 0
for item in farmer_data['仕入先']:
  idx += 1
  farmer_idx.append('F' + str(idx))

# キーを付与
farmer_data.insert(0, '仕入先ID', farmer_idx)

# 商品データを別のデータフレームに格納
product_data = input_data[['商品','販売単価']].copy()
product_data.drop_duplicates(inplace=True)

# 商品のキーを生成
product_idx = []
idx = 0
for item in product_data['商品']:
  idx += 1
  product_idx.append('P' + str(idx))

# キーを付与
product_data.insert(0, '商品ID', product_idx)

# 取引テーブルをキーに変換
order_data = pd.merge(input_data, farmer_data[['仕入先ID', '仕入先']], how='left', on='仕入先')
order_data = pd.merge(order_data, product_data[['商品ID', '商品']], how='left', on='商品')
order_data = order_data[['仕入先ID','商品ID', '入荷日']]
order_data

# %% id="68Sp2DkUKGnY" executionInfo={"status": "ok", "timestamp": 1654455158813, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# 各データフレームをファイルに出力
order_data.to_csv('12-3_order.csv', index=False)
farmer_data.to_csv('12-3_farmer.csv', index=False)
product_data.to_csv('12-3_product.csv', index=False)

# %% [markdown] id="zaZUByOlAbIz"
# ### 放課後ノック１１４： 外れ値の加工に挑戦

# %% id="Pn1xHZf-AbIz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1654455159060, "user_tz": -540, "elapsed": 251, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ff9ba918-8548-4d79-b352-81b07bf5ec04"
# csvファイルの読み込み
input_data = pd.read_csv("12-4.csv")
input_data['金額'].describe().astype('int')

# %% id="mNCnoV63AbIz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1654455159060, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="91ab107a-2c37-4cea-aa78-9dfc6fb162bb"
# 第３四分位数を取得
threshold = input_data['金額'].quantile(0.75)

# 第３四分位数を超えたデータを第３四分位数で置き換える
output_data = input_data.copy()
output_data.loc[input_data['金額']>threshold, '金額'] = threshold
output_data['金額'].describe()

# %% id="j2F3y2DEapoB" executionInfo={"status": "ok", "timestamp": 1654455159381, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
output_data['金額'].describe().to_csv('12-4_out.csv')

# %% [markdown] id="QvALpZfPAbI1"
# ### 放課後ノック１１５： 欠損値の補完に挑戦

# %% id="B2GmAaaTAbI1" colab={"base_uri": "https://localhost:8080/", "height": 959} executionInfo={"status": "ok", "timestamp": 1654455160152, "user_tz": -540, "elapsed": 513, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="a75520d6-f5e5-4209-abdd-7d18d3dc272f"
# エクセルファイルの読み込み
input_data = pd.read_excel("12-5.xlsx")
input_data

# %% id="JTuHJmjsAbI1" colab={"base_uri": "https://localhost:8080/", "height": 959} executionInfo={"status": "ok", "timestamp": 1654455160688, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="84291316-be58-4a22-e27d-bea3eb10fef2"
import math
output_data = input_data.copy()

# 都道府県の欠損データを補完
target_div = output_data.loc[output_data['都道府県'].isnull(), '市区町村']
for division in target_div:
  output_data.loc[(output_data['都道府県'].isnull()) & (output_data['市区町村']==division), '都道府県'] = output_data.loc[(output_data['市区町村']==division) & ~(output_data['都道府県'].isnull()), '都道府県'].unique()[0]

# 年齢の欠損データを補完
target_div = output_data.loc[output_data['年齢'].isnull(), '市区町村']
for division in target_div:
  output_data.loc[(output_data['年齢'].isnull()) & (output_data['市区町村']==division), '年齢'] = math.floor(output_data.loc[output_data['市区町村']==division, '年齢'].mean())

output_data

# %% id="997-_YzbAbI2" executionInfo={"status": "ok", "timestamp": 1654455160689, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvファイルに出力
output_data.to_csv('12-5_out.csv', index=False)

# %% [markdown] id="4FzUOIHfAbI2"
# ### 放課後ノック１１６： データのスクランブル化に挑戦

# %% id="n-JT3pCPAbI3" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1654455160962, "user_tz": -540, "elapsed": 279, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3800d883-c4df-4b82-c04d-3357ecfb0b49"
# エクセルファイルの読み込み
input_data = pd.read_excel("12-6.xlsx")
input_data.head()

# %% id="C1SylLOOAbI3" colab={"base_uri": "https://localhost:8080/", "height": 394} executionInfo={"status": "ok", "timestamp": 1654455161355, "user_tz": -540, "elapsed": 397, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="31fce780-ee8b-40da-e4cd-c03cf5a91016"
# スクランブル前の合計を検証のために表示
input_data.groupby('氏名').sum()

# %% id="m2MtxaiXAbI3" colab={"base_uri": "https://localhost:8080/", "height": 394} executionInfo={"status": "ok", "timestamp": 1654455161356, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="2329b4ff-5821-4fb4-f4ff-5720eec669b8"
import hashlib
output_data = input_data.copy()

# 氏名をハッシュ化
output_data['氏名'] = output_data['氏名'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
# ハッシュ化した氏名で集計
output_data.groupby('氏名').sum()

# %% id="HVbdSNGr66Ga" executionInfo={"status": "ok", "timestamp": 1654455161357, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvファイルに出力
output_data.groupby('氏名').sum().to_csv('12-6_out.csv')

# %% [markdown] id="rLINqt9UAbI3"
# ### 放課後ノック１１７： 文字コードの自動判定に挑戦

# %% id="hWDSGqf2AbI3" colab={"base_uri": "https://localhost:8080/", "height": 143} executionInfo={"status": "ok", "timestamp": 1654455162595, "user_tz": -540, "elapsed": 869, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e70cd82a-6f05-4dae-8f67-fa9f75be38bb"
# ファイルの文字コードを調べる
import chardet

files = ['12-7-1.csv', '12-7-2.csv', '12-7-3.csv']
df = pd.DataFrame()

for file in files:
  # バイナリでファイルを開く
  with open(file, mode='rb') as f:
    contents = f.read()
    enc = chardet.detect(contents)['encoding']
    # 判明した文字コードでファイルを読み込む
    df = pd.concat([df, pd.read_csv(file, encoding=enc)])

df

# %% id="bFdWuhffAbI4" executionInfo={"status": "ok", "timestamp": 1654455162595, "user_tz": -540, "elapsed": 3, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvファイルに出力
df.to_csv('12-7_out.csv', index=False)

# %% [markdown] id="8VHb8RqWAbI4"
# ### 放課後ノック１１８： センサーデータの加工に挑戦

# %% id="CyU0ijjMAbI4" colab={"base_uri": "https://localhost:8080/", "height": 458} executionInfo={"status": "ok", "timestamp": 1654455164129, "user_tz": -540, "elapsed": 1538, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="b1124482-2c8e-404f-ed40-78da5f31e485"
sensor1 = pd.read_csv('12-8-1.csv', index_col=0)
sensor2 = pd.read_csv('12-8-2.csv', index_col=0)

display(sensor1.head())
display(sensor2.head())

# %% id="qIJIRn3uHXv0" colab={"base_uri": "https://localhost:8080/", "height": 455} executionInfo={"status": "ok", "timestamp": 1654455164130, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="1a474d2b-52c9-42c7-db17-3ec07ab024c3"
# 2つのセンサー値を結合し、タイムスタンプで並び替え
df_main = pd.concat([sensor1, sensor2], ignore_index=False)
df_main.sort_values('time_stamp', inplace=True)

# 欠損値を線形補間
df_main.interpolate(method='linear', inplace=True)

# 1行目は補間できないので、０とする
df_main.iat[0,0] = 0
df_main.iat[0,1] = 0

df_main

# %% id="cTqRh8q0HbdU" executionInfo={"status": "ok", "timestamp": 1654455164130, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvファイルに出力
df_main.to_csv('12-8_out.csv')

# %% [markdown] id="m41ZViEfAbI5"
# ### 放課後ノック１１９： JSON形式に挑戦

# %% id="IB3ENIsPAbI5" colab={"base_uri": "https://localhost:8080/", "height": 771} executionInfo={"status": "ok", "timestamp": 1654455164538, "user_tz": -540, "elapsed": 412, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="9311930c-9680-41c1-80ec-74de08cb3863"
# csvファイルの読み込み
input_data = pd.read_csv("12-9.csv")
input_data

# %% id="1H_LQgm3AbI5" executionInfo={"status": "ok", "timestamp": 1654455164539, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# JSONに変換しファイル出力
import json
input_data.to_json('12-9.json')

# %% id="19YEkeZoTY0c" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1654455164539, "user_tz": -540, "elapsed": 11, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="ee2f9019-f6c3-474d-b110-08b51e98aa14"
# JSON形式のファイルを直接データフレームに読み込み
read_json = pd.read_json('12-9.json')
read_json.head()

# %% id="OHCII73zT3Ut" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1654455164539, "user_tz": -540, "elapsed": 10, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="861d19d6-f905-47a1-d19b-a88e207cd3ec"
# JSON形式のファイルを辞書形式で読み込み
with open('12-9.json') as f:
  dict_json = json.load(f)
dict_json

# %% [markdown] id="BlbjCMdTAbI5"
# ### 放課後ノック１２０： SQLiteに挑戦

# %% id="yx55jXOEAbI5" executionInfo={"status": "ok", "timestamp": 1654455164871, "user_tz": -540, "elapsed": 339, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# SQLiteライブラリのインポート
import sqlite3

# データベース名（任意の名前.db）
db_name = 'TrialDatabase.db'
# データベースに接続（データベースが存在しない場合はデータベースを生成して接続）
con = sqlite3.connect(db_name)
cur = con.cursor()
# 成功すると、db_nameで定義したデータベースがファイルとしてドライブに存在していると思います。確認してみて下さい。

# %% id="p2vpR7NEAbI5" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1654455164871, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="3df98f97-89a3-4dd1-8d3c-10d3b5e6fef2"
# csvファイルの読み込み
input_data = pd.read_csv("12-9.csv")
input_data.head()

# %% id="Xks4XZBlcaHg" executionInfo={"status": "ok", "timestamp": 1654455167596, "user_tz": -540, "elapsed": 656, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvの情報をテーブルに格納（データフレームのto_sqlでテーブルが作成され、データが入ります！簡単！）
input_data.to_sql('t_data', con, if_exists='replace', index=None)

# %% id="qCjjo6FbAbI5" colab={"base_uri": "https://localhost:8080/", "height": 771} executionInfo={"status": "ok", "timestamp": 1654455167849, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="e64f00cd-3844-4f43-88bb-f462a24ad9e1"
# 抽出クエリ（SELECT句）でデータベースに問い合わせ、結果をデータフレーム型で受け取る
sql = 'select * from t_data;'
df = pd.read_sql_query(sql, con)
df

# %% id="C2Y4g5WDdaUK" executionInfo={"status": "ok", "timestamp": 1654455168612, "user_tz": -540, "elapsed": 2, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
# csvファイルに出力
df.to_csv('12-10_out.csv', index=False)

# %% id="IpUtBVHlNmvB"
