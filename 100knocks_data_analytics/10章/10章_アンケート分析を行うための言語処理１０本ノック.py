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

# %% id="Uexmpj7_MnE9"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="00tgumtZMoJq"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/10章') #ここを変更。

# %% [markdown] id="t2MO76FbMmTW"
# # 10章 アンケート分析を行うための言語処理１０本ノック
#
# ここでは、まちづくりのアンケートを使って分析していきます。  
# 主に言語処理を取り扱っていきます。
# 言語処理特有の処理や、データの持たせ方を学びましょう。

# %% [markdown] id="ABqHf2VzMmTY"
# ### ノック91：データを読み込んで把握しよう

# %% id="NgpqvHYGMmTY"

# %% id="jF2HtNmzMmTY"

# %% id="tVwr8QvvMmTZ"

# %% [markdown] id="A2UBM9W2MmTZ"
# ### ノック92：不要な文字を除外してみよう

# %% id="93H0jLtlMmTZ"

# %% id="sT82t8WNMmTZ"

# %% id="8UgcH-2pMmTZ"

# %% id="zZDlQgD_MmTZ"

# %% [markdown] id="9i_sW01pMmTZ"
# ### ノック93：文字数をカウントしてヒストグラムを表示してみよう

# %% id="zhkenrCwMmTZ"

# %% id="s4HleWCfMmTZ"

# %% [markdown] id="mq-2tNj8MmTa"
# ### ノック94：形態素解析で文章を分割してみよう

# %% id="6EcXDulaMmTa"

# %% id="a64RGS0YMmTa"

# %% [markdown] id="MEa1EuymMmTa"
# ### ノック95：形態素解析で文章から「動詞・名詞」を抽出してみよう

# %% id="n1VUddclMmTa"

# %% [markdown] id="b2gHS33GMmTa"
# ### ノック96：形態素解析で抽出した頻出する名詞を確認してみよう

# %% id="2_y6jLchMmTa"

# %% id="qehb9KpyMmTa"

# %% [markdown] id="0_GFAxpJMmTa"
# ### ノック97：関係のない単語を除去しよう

# %% id="N3E4iZRdMmTa"

# %% id="kIKjHEP0MmTa"

# %% [markdown] id="46KpIxkrMmTa"
# ### ノック98：顧客満足度と頻出単語の関係をみてみよう

# %% id="GzftnlntMmTb"

# %% id="WIps1twXMmTb"

# %% id="8te6UyVcMmTb"

# %% id="foOZK6NEMmTb"

# %% [markdown] id="HB070vImMmTb"
# ### ノック99：アンケート毎の特徴を表現してみよう

# %% id="ZtHnQ07zMmTb"

# %% id="XiBhFyKdMmTb"

# %% [markdown] id="zA_67OzTMmTb"
# ### ノック100：類似アンケートを探してみよう

# %% id="snrqNhqaMmTb"

# %% id="G1D4pgkbMmTb"

# %% id="ro4fr0rQMmTb"
