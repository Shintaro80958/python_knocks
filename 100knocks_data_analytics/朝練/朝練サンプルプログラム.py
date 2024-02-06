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
#     name: python3
# ---

# %% id="3YE65Askt36F"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="qF-_KhBBuLa9"
# 作業フォルダへの移動を行います。
# 人によって作業場所が異なるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/朝練') #ここを変更。

# %% [markdown] id="Wva6tCGU3gxb"
# # 朝練 サンプルプログラム
#
# Googleドライブにあるcsvファイルを、Pandasライブラリを用いて読み込みを行います。

# %% id="TdX1ViGd2nWL"
import pandas as pd

# %% id="oRggwvdz0d74"
file = 'height_data.csv'
# ファイルの読み込み
df = pd.read_csv(file)

# %% id="9MuNqqAY38Xd"
# 表示処理
df.head()

# %% id="Kz8KVBFn1nxl"
