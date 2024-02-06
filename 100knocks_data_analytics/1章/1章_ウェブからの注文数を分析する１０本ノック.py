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

# %% id="WlS8LwC8J3kd"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="G-vAUZn2J52N"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/1章') #ここを変更。

# %% [markdown] id="qUQ5OkKmJ1mJ"
# # １章 ウェブの注文数を分析する１０本ノック
#
# ここでは、ある企業のECサイトでの商品の注文数の推移を分析していきます。  
# データの属性を理解し、分析をするためにデータを加工した後、  
# データの可視化を行うことで問題を発見していくプロセスを学びます。

# %% [markdown] id="HyMoAlu5J1mN"
# ### ノック１：データを読み込んでみよう

# %% id="Wicqn13lJ1mO"

# %% id="rJm5rP2uJ1mP"

# %% id="iPazmB_tJ1mP"

# %% id="13Byx1zPJ1mQ"

# %% [markdown] id="tUj49Lq2J1mQ"
# ### ノック２：データを結合(ユニオン)してみよう

# %% id="yToHeaCkJ1mR"

# %% id="nIlKzMwUJ1mS"

# %% id="UI1QoncnJ1mS"

# %% [markdown] id="hL_2eEJsJ1mS"
# ### ノック３：売上データ同士を結合(ジョイン)してみよう

# %% id="cM5Iq_32J1mT"

# %% id="dEIa14ICJ1mT"

# %% [markdown] id="N68ukZAbJ1mT"
# ### ノック４：マスタデータを結合(ジョイン)してみよう

# %% id="jAi74QxfJ1mT"

# %% [markdown] id="PC6cvtpvJ1mT"
# ### ノック5：必要なデータ列を作ろう

# %% id="7oTFxMNsJ1mU"

# %% [markdown] id="9_CDTQ9OJ1mU"
# ### ノック6：データ検算をしよう

# %% id="F7hNI74PJ1mU"

# %% id="hP3vtiFGJ1mU"

# %% [markdown] id="SUIoReEXJ1mU"
# ### ノック7：各種統計量を把握しよう

# %% id="ybIheNP9J1mV"

# %% id="XeY8QOZ0J1mV"

# %% id="WvF_-kmuJ1mV"

# %% [markdown] id="IWYKOREPJ1mV"
# ### ノック8：月別でデータを集計してみよう

# %% id="s3ljKRbsJ1mV"

# %% id="gFaE0moTJ1mV"

# %% id="e1VQDr9dJ1mV"

# %% [markdown] id="NEsEIEtWJ1mV"
# ### ノック9：月別、商品別でデータを集計してみよう

# %% id="aZyzr_vIJ1mW"

# %% id="L2zR-vGTJ1mW"

# %% [markdown] id="7RXaPfePJ1mW"
# ### ノック10：商品別の売上推移を可視化してみよう

# %% id="JG1yWhO7J1mW"

# %% id="NWudJq7YJ1mW"

# %% id="xeQcyLAXJ1mW"
