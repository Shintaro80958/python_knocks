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

# %% id="wisOAvS-Kfs8"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="FUXzthcCKgjh"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/4章') #ここを変更。

# %% [markdown] id="jYL91FIdKeoL"
# # 4章 顧客の全体像を把握する１０本ノック
#
# 引き続き、スポーツジムの会員データを使って顧客の行動を分析していきます。  
# ３章で顧客の全体像を把握しました。  
# ここからは、機械学習を用いて顧客のグループ化や顧客の利用予測行なっていきましょう。  
# ここでは、教師なし学習、教師あり学習の回帰を取り扱います。

# %% [markdown] id="yOb4kRGAKeoM"
# ### ノック31：データを読み込んで確認しよう

# %% id="QHDi7dtjKeoN"

# %% id="jOvUjwKLKeoN"

# %% [markdown] id="Tx1_r3WVKeoN"
# ### ノック32：クラスタリングで顧客をグループ化しよう

# %% id="v37y05qmKeoN"

# %% id="1mVCJS_WKeoO"

# %% [markdown] id="foZ8rqCvKeoO"
# ### ノック33：クラスタリング結果を分析しよう

# %% id="QiBTnCqrKeoO"

# %% id="xIVQIAdZKeoO"

# %% [markdown] id="LsaWC_VvKeoO"
# ### ノック34：クラスタリング結果を可視化してみよう

# %% id="LoNK5gkiKeoO"

# %% id="OPq51pnPKeoO"

# %% [markdown] id="zYbJeeZPKeoO"
# ### ノック35：クラスタリング結果をもとに退会顧客の傾向を把握しよう

# %% id="4mUYlAg2KeoO"

# %% id="HnmlTXFvKeoO"

# %% [markdown] id="AZu4lMlDKeoP"
# ### ノック36：翌月の利用回数予測を行うためのデータ準備をしよう

# %% id="qniHeNbBKeoP"

# %% id="_zu8UyDdKeoP"

# %% id="6Ep9MUMyKeoP"

# %% [markdown] id="0363GVNBKeoP"
# ### ノック37：特徴となる変数を付与しよう

# %% id="E8KNtSQcKeoP"

# %% id="OmzWAKhfKeoP"

# %% [markdown] id="GGfFoF_xKeoP"
# ### ノック38：来月の利用回数予測モデルを作成しよう

# %% id="P6L50G3-KeoP"

# %% id="LIAmmAdBKeoP"

# %% [markdown] id="3a6svnM2KeoP"
# ### ノック39：モデルに寄与している変数を確認しよう

# %% id="FK0HFJnRKeoP"

# %% [markdown] id="eSD3iI9vKeoP"
# ### ノック40：来月の利用回数を予測しよう

# %% id="SxPgLdS1KeoP"

# %% id="O8-juwaUKeoQ"

# %% id="E9xiygOIKeoQ"
