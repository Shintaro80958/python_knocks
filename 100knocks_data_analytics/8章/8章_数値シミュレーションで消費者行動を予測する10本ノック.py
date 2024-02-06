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

# %% id="y8UuWTOSL4c1"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="sZkOlL3OL5k3"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/8章') #ここを変更。

# %% [markdown] id="XgId55J8XLT3"
# # 8章 数値シミュレーションで消費者行動を予測する10本ノック
#
# ここでは、消費者行動が口コミなどの情報伝播によってどのように変化していくかを分析する、  
# 人間関係のネットワーク構造を用いた数値シミュレーション手法を中心に学んでいきます。

# %% [markdown] id="stY2jCebXLT4"
# ### ノック71：人間関係のネットワークを可視化してみよう

# %% id="OQV_NGcDXLT4"

# %% id="tPkKAYFgXLT5"

# %% [markdown] id="p3KgUifTXLT6"
# ### ノック72：口コミによる情報伝播の様子を可視化してみよう

# %% id="wYzhjCfdXLT6"

# %% id="Surk1RO5XLT7"

# %% id="i2ftpTFIXLT7"

# %% id="eTdeSqs5XLT8"

# %% id="QX5LBm-FXLT8"

# %% id="iaicAtBPXLT8"

# %% id="z2Vc5nrjXLT8"

# %% id="bzCI3hs4XLT9"

# %% [markdown] id="Zwgb3cltXLT9"
# ### ノック73：口コミ数の時系列変化をグラフ化してみよう

# %% id="wd9O5KJzXLT9"

# %% [markdown] id="z-1MQQnQXLT9"
# ### ノック74：会員数の時系列変化をシミュレーションしてみよう

# %% id="rLHAXrRRXLT9"

# %% id="WeCwSkWjXLT-"

# %% id="qhOiUoY6XLT-"

# %% id="FkJ2Sr3zXLT-"

# %% id="aMkMjqV_XLT-"

# %% [markdown] id="nNY5RxPDXLT-"
# ### ノック75：パラメータの全体像を相図を見ながら把握しよう

# %% id="1RV9llkYXLT_"

# %% id="Yx27DrAEXLT_"

# %% [markdown] id="EN7NtQd_XLT_"
# ### ノック76：実データを読み込んでみよう

# %% id="cnf1JOAUXLT_"

# %% [markdown] id="WoBNPvATXLT_"
# ### ノック77：リンク数の分布を可視化しよう

# %% id="e50QK2tiXLT_"

# %% id="yL0V1rSRXLT_"

# %% [markdown] id="E-X1IexRXLUA"
# ### ノック78：シミュレーションのために実データからパラメータを推定しよう

# %% id="ZMsE4Z5DXLUA"

# %% id="jVqvee6eXLUA"

# %% id="_Jv9x-i1XLUA"

# %% id="Py6kvOngXLUA"

# %% [markdown] id="LeMY5ekeXLUA"
# ### ノック79：実データとシミュレーションを比較しよう

# %% colab={"background_save": true} id="nDLCDF18XLUA"

# %% colab={"background_save": true} id="4md0CTXTXLUA"

# %% colab={"background_save": true} id="NXG8sZR8XLUA"

# %% colab={"background_save": true} id="4wHNMScDXLUB"

# %% [markdown] id="CVNR8gL-XLUB"
# ### ノック80：シミュレーションによる将来予測を実施しよう

# %% colab={"background_save": true} id="jmsJKX5SXLUB"

# %% colab={"background_save": true} id="PLerEPkpXLUB"

# %% id="TjPYx6FKXLUB"
