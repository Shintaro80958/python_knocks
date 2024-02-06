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

# %% id="EMADV4pYNK-K"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="BnsrGBPcNOZU"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/11章') #ここを変更。

# %% [markdown] id="tIPfsEyjgiuX"
# # 11章　深層学習に挑戦する10本ノック
# ここでは、深層学習を学ぶうえで必要なプログラムを実行していく流れを学んでいきます。

# %% [markdown] id="yQk7qjQDgiuX"
# ### 放課後ノック101：深層学習に必要なデータを準備しよう

# %% id="EPclN4iJEC9D"

# %% [markdown] id="ZlYnr8W4B_ep"
# ### データを読み込んでみよう

# %% id="Yf_s5y7sBjVm"

# %% [markdown] id="LYD3v9NdKjja"
# ### データを確認しよう

# %% id="rpOEx4H9B5d6"

# %% id="w8iMJZlZCOmm"

# %% id="V6cF37hMEruO"

# %% id="_Y9STzkzEeWq"

# %% id="7xB4aVz2Emjo"

# %% [markdown] id="e1uozuVUFpbz"
# ### データを準備しよう

# %% id="E4it4lD4Flj0"

# %% id="9zOWf_aiFlm2"

# %% [markdown] id="Rb_rHk92Cut0"
# ### 放課後ノック102：深層学習モデルを構築しよう

# %% [markdown] id="bsIAbTXiLIIm"
# ### ニューラルネットワークモデルを定義しよう

# %% id="SCjUD0AEHrzA"

# %% id="AJtFKA6OIq0x"

# %% [markdown] id="EG_BP8XhLNUx"
# ### CNNモデルを定義しよう

# %% id="UX_YasFwCuV6"

# %% id="qRfIvakXDWT3"

# %% [markdown] id="9QPT0NxULbcP"
# ### ニューラルネットワークモデルを構築しよう

# %% id="Sy0dI8PFDYfg"

# %% [markdown] id="Y78F7NLJLh6s"
# ### CNNモデルを構築しよう

# %% id="lnYJX0G8I0BC"

# %% [markdown] id="5yvrKBWjIYlI"
# ### 放課後ノック103：モデルの評価をしてみよう

# %% id="aA8W7V7tFQLC"

# %% id="V6yq8QWeGaGo"

# %% [markdown] id="AJEmYkbeMWe0"
# ### 放課後ノック104：モデルを使った予測をしてみよう

# %% id="hEajnTfDKEZu"

# %% id="p-VZIi18KfqY"

# %% id="4LANj-i-WQoF"

# %% id="ricZ2KjHKitr"

# %% id="URUMqxERKmGj"

# %% id="Cgo4mdhmrJao"

# %% [markdown] id="UpmS7--w4YZF"
# ### 放課後ノック105：物体検出YOLOを使って人の検出を行ってみよう

# %% [markdown] id="Eb7OfRtBvKUC"
# ### YOLOの準備

# %% id="FAKvqj2XnQj-"

# %% id="k5BjFMFnn7Za"

# %% id="eByPqawwoVc7"

# %% [markdown] id="DKPYmAp-wvtJ"
# ### YOLOによる物体検出の実行

# %% id="_Hp9rZ5q1Iay"

# %% id="R2bBDwf61Ip8"

# %% id="J0_NTn0P_VWC"

# %% [markdown] id="ZS5abmZ7xBQ_"
# ### 結果の出力

# %% id="rpFo8yPt_dte"

# %% [markdown] id="WFl2r6FDt_P1"
# ### 放課後ノック106：YOLOの学習を行うための準備をしよう

# %% [markdown] id="XCWodp_mxrvG"
# ### 学習データのダウンロード

# %% id="g_sBaX_5nJBz"

# %% [markdown] id="zim5JC_jxviJ"
# ### 学習データの確認

# %% id="ZRSb05V_ryGC"

# %% id="-7-aAtnWryIi"

# %% [markdown] id="8WeCtG4VxkEZ"
# ### 放課後ノック107：新たな学習データを使ってYOLOの学習モデルを生成してみよう

# %% [markdown] id="scd8ku8ix3-n"
# ### ライブラリのインストール

# %% id="19AfE-oBoywW"

# %% [markdown] id="t2E8AJvSx7a8"
# ### 学習データの変換

# %% id="jLnLblWMqm2p"

# %% [markdown] id="F-xxvU37yPJZ"
# ### 学習データ読み込みクラスの定義

# %% id="QlyQ5j_PoXPa"



# %% [markdown] id="FmImgsydy7QY"
# ### YOLOモデル(ネットワーク)の読み込み

# %% id="pT83GAyExapw"

# %% id="7uv8wOy-yJfO"

# %% [markdown] id="UySDjHGW0BHf"
# ### 学習データの読み込み

# %% id="K5xgUKjiyRSQ"

# %% [markdown] id="PiVSTcSr0ErM"
# ### 学習の実施

# %% id="rQrv-F_YyW6f"

# %% id="yHdcPhz_yZXU"

# %% [markdown] id="3OqkGbOW3c6i"
# ### 放課後ノック108：新たに学習させたモデルを使って人の検出を行ってみよう

# %% [markdown] id="cK8VHMiO0zr1"
# ### 学習した重みの読み込み

# %% id="1j2EScKY12gx"

# %% id="XizpUkI11IdK"

# %% [markdown] id="IdcccUPa03cN"
# ### 物体検出の実行

# %% id="smr62Jkw1Ifq"

# %% [markdown] id="aDmfgGLI1FkX"
# ### 結果の表示

# %% id="iKiCvBwC1Ih4"

# %% [markdown] id="KMterp_J1cgF"
# ### 放課後ノック109：YOLOとHOGの人の検出結果を比較して深層学習の精度を体感しよう

# %% [markdown] id="44hQiGY623G_"
# ### HOGによる人の検出

# %% id="FKujwzGC1g1k"

# %% [markdown] id="8hsy8O-u5t6B"
# ### 結果の比較

# %% id="RIQp-9Oq1g8c"

# %% [markdown] id="wGdqlEqWNUYd"
# ### 放課後ノック110：YOLOでの人以外の物体の検出のようすを確認しよう

# %% id="OmVe83TRNlSF"
