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

# %% id="PXQilQBDK2zI"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="mE4u7jHDK89y"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/5章') #ここを変更。

# %% [markdown] id="QVgZ6zKJK12a"
# # 5章 顧客の退会を予測する１０本ノック
#
# 引き続き、スポーツジムの会員データを使って顧客の行動を分析していきます。  
# ３章では顧客の全体像を把握し、4章では数ヶ月利用している顧客の来月の利用回数の予測を行いました。   
# ここでは、教師あり学習の分類を用いて、顧客の退会予測を取り扱います。

# %% [markdown] id="2JCN2_DzK12b"
# ### ノック41：データを読み込んで利用データを整形しよう

# %% id="K6H_cRrYK12c"

# %% id="qtOfE3SwK12c"

# %% [markdown] id="SBJXU_W5K12c"
# ### ノック42：退会前月の退会顧客データを作成しよう

# %% id="uXUzFH-sK12c"

# %% id="tlGQwSd6K12c"

# %% [markdown] id="9XVuswybK12c"
# ### ノック43：継続顧客のデータを作成しよう

# %% id="NkfGkFpfK12d"

# %% id="JetZqZrzK12d"

# %% id="T5ka47YNK12d"

# %% [markdown] id="ZI0H0yAJK12d"
# ### ノック44：予測する月の在籍期間を作成しよう

# %% id="iaHwI60JK12d"

# %% [markdown] id="H3XgfzYUK12d"
# ### ノック45：欠損値を除去しよう

# %% id="XT2hAbyVK12e"

# %% id="73v7k5jAK12e"

# %% [markdown] id="MqYmEu0wK12e"
# ### ノック46：文字列型の変数を処理できるように整形しよう

# %% id="1otlh1fKK12e"

# %% id="bmmdxrQVK12e"

# %% id="KwBeA7UbK12e"

# %% [markdown] id="Hf3UnyunK12e"
# ### ノック47：決定木を用いて退会予測モデルを作成してみよう

# %% id="mdwuSmPcK12e"

# %% id="qYyD8LItK12e"

# %% [markdown] id="wls9B2RoK12e"
# ### ノック48：予測モデルの評価を行ない、モデルのチューニングをしてみよう

# %% id="UCkURwOSK12f"

# %% id="6OxtgjVDK12f"

# %% id="hsYkSnzsK12f"

# %% [markdown] id="gJH8P0SmK12f"
# ### ノック49：モデルに寄与している変数を確認しよう

# %% id="d_9X7WtiK12f"

# %% [markdown] id="wK-2_5xtK12f"
# ### ノック50：顧客の退会を予測しよう

# %% id="5MNshD5NK12f"

# %% id="thR5qOs5K12f"

# %% id="Hw4PWBZ9K12f"

# %% id="KKftbWJZK12f"
