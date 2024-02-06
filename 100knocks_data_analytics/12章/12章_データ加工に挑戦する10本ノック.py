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

# %% id="vF_JshRtAfOp"
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

# %% id="BVYPHVH3xAsa"

# %% id="qi6XXxsyAbIu" colab={"base_uri": "https://localhost:8080/", "height": 206} executionInfo={"status": "ok", "timestamp": 1654455157512, "user_tz": -540, "elapsed": 1049, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="800d6d32-01ff-4f0c-e4bf-1a2d358e994d"

# %% id="0NfqK54_AbIv" colab={"base_uri": "https://localhost:8080/", "height": 175} executionInfo={"status": "ok", "timestamp": 1654455157513, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="6b273615-d49a-4163-a496-dcc0fa2041c4"

# %% id="AL-wmJscwavr"

# %% [markdown] id="-kiPZP1AAbIv"
# ### 放課後ノック１１２： エクセルの社員マスタ加工に挑戦

# %% id="YpYFUtvFAbIw" colab={"base_uri": "https://localhost:8080/", "height": 332} executionInfo={"status": "ok", "timestamp": 1654455157877, "user_tz": -540, "elapsed": 368, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}} outputId="cb24e7c5-f8b3-4059-baef-ac1c95649f06"

# %% id="wrzVsWI3AbIw" executionInfo={"status": "ok", "timestamp": 1654455506584, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="5-eR9XYZ-5Af" executionInfo={"status": "ok", "timestamp": 1654455506585, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="6j4JAl_uAbIx"
# ### 放課後ノック１１３： 正規化に挑戦

# %% id="N5pLAkwZAbIy" executionInfo={"status": "ok", "timestamp": 1654455506585, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="d4MEUWc8AbIy" executionInfo={"status": "ok", "timestamp": 1654455506585, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="68Sp2DkUKGnY" executionInfo={"status": "ok", "timestamp": 1654455506585, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="zaZUByOlAbIz"
# ### 放課後ノック１１４： 外れ値の加工に挑戦

# %% id="Pn1xHZf-AbIz" executionInfo={"status": "ok", "timestamp": 1654455506586, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="mNCnoV63AbIz" executionInfo={"status": "ok", "timestamp": 1654455506586, "user_tz": -540, "elapsed": 4, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="j2F3y2DEapoB" executionInfo={"status": "ok", "timestamp": 1654455506975, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="QvALpZfPAbI1"
# ### 放課後ノック１１５： 欠損値の補完に挑戦

# %% id="B2GmAaaTAbI1" executionInfo={"status": "ok", "timestamp": 1654455506976, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="JTuHJmjsAbI1" executionInfo={"status": "ok", "timestamp": 1654455506976, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="997-_YzbAbI2" executionInfo={"status": "ok", "timestamp": 1654455506977, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="4FzUOIHfAbI2"
# ### 放課後ノック１１６： データのスクランブル化に挑戦

# %% id="n-JT3pCPAbI3" executionInfo={"status": "ok", "timestamp": 1654455506977, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="C1SylLOOAbI3" executionInfo={"status": "ok", "timestamp": 1654455506977, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="m2MtxaiXAbI3" executionInfo={"status": "ok", "timestamp": 1654455506978, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="HVbdSNGr66Ga" executionInfo={"status": "ok", "timestamp": 1654455506978, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="rLINqt9UAbI3"
# ### 放課後ノック１１７： 文字コードの自動判定に挑戦

# %% id="hWDSGqf2AbI3" executionInfo={"status": "ok", "timestamp": 1654455506979, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="bFdWuhffAbI4" executionInfo={"status": "ok", "timestamp": 1654455506979, "user_tz": -540, "elapsed": 7, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="8VHb8RqWAbI4"
# ### 放課後ノック１１８： センサーデータの加工に挑戦

# %% id="CyU0ijjMAbI4" executionInfo={"status": "ok", "timestamp": 1654455507384, "user_tz": -540, "elapsed": 412, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="qIJIRn3uHXv0" executionInfo={"status": "ok", "timestamp": 1654455507385, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="cTqRh8q0HbdU" executionInfo={"status": "ok", "timestamp": 1654455507385, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="m41ZViEfAbI5"
# ### 放課後ノック１１９： JSON形式に挑戦

# %% id="IB3ENIsPAbI5" executionInfo={"status": "ok", "timestamp": 1654455507385, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="1H_LQgm3AbI5" executionInfo={"status": "ok", "timestamp": 1654455507385, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="19YEkeZoTY0c" executionInfo={"status": "ok", "timestamp": 1654455507385, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="OHCII73zT3Ut" executionInfo={"status": "ok", "timestamp": 1654455507386, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% [markdown] id="BlbjCMdTAbI5"
# ### 放課後ノック１２０： SQLiteに挑戦

# %% id="yx55jXOEAbI5" executionInfo={"status": "ok", "timestamp": 1654455507386, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="p2vpR7NEAbI5" executionInfo={"status": "ok", "timestamp": 1654455507386, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="Xks4XZBlcaHg" executionInfo={"status": "ok", "timestamp": 1654455507386, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}

# %% id="qCjjo6FbAbI5" executionInfo={"status": "ok", "timestamp": 1654455507386, "user_tz": -540, "elapsed": 5, "user": {"displayName": "\u4e0b\u5c71\u8f1d\u660c", "userId": "17333420985264756541"}}
