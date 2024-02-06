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

# %% id="ZEZFeC07MUe2"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="PUrDM-fnMVyC"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/9章') #ここを変更。

# %% [markdown] id="m8fW5dtcMUCJ"
# # 9章 潜在顧客を把握するための画像認識１０本
#
# ここでは、カメラから取得した映像を用いて画像認識を行い、  
# 必要な情報を取得するための流れを学ぶことで、  
# 画像認識をビジネス現場で応用するイメージをつかみます。

# %% [markdown] id="_WgAWNzNMUCM"
# ### ノック８１：画像データを読み込んでみよう

# %% id="rVsF2N54MUCN"

# %% [markdown] id="TISvxrOfMUCN"
# ### ノック８２：映像データを読み込んでみよう

# %% id="a-oX2XaXMUCN"

# %% [markdown] id="pz_rXWMhMUCO"
# ### ノック８３：映像を画像に分割し、保存してみよう

# %% id="9BPwW8sOMUCO"

# %% [markdown] id="RBdoBYs1MUCO"
# ### ノック８４：画像内のどこに人がいるのかを検出してみよう

# %% id="NiIvyohmMUCP"

# %% [markdown] id="-IHX4_OTMUCP"
# ### ノック８５：画像内の人の顔を検出してみよう

# %% id="6VpwVOtAMUCP"

# %% [markdown] id="FYe398h1MUCP"
# ### ノック８６：画像内の人がどこに顔を向けているのかを検出してみよう

# %% id="1ywr23qoMUCQ"

# %% [markdown] id="e2ue3V4iMUCQ"
# ### ノック８７：検出した情報を統合し、タイムラプスを作ってみよう

# %% id="EAuTarQ7MUCQ"

# %% [markdown] id="Cwh0BxxEMUCQ"
# ### ノック８８：全体像をグラフにして可視化してみよう

# %% id="pCKa0a2NMUCQ"

# %% id="HekkcCIoMUCQ"

# %% [markdown] id="HctMTWNLMUCR"
# ### ノック８９：人通りの変化をグラフで確認しよう

# %% id="y2IBXEyYMUCR"

# %% id="f1wLnbD2MUCR"

# %% [markdown] id="eVhP5D1yMUCR"
# ### ノック９０：移動平均を計算することでノイズの影響を除去しよう

# %% id="kJLzpEo5MUCR"

# %% id="yJZE3X1KMUCR"

# %% id="hxbAsr9tMUCR"

# %% id="BSrhPoGiMUCR"
