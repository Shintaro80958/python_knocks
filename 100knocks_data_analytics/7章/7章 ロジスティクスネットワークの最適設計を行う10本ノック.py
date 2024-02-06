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

# %% id="uk5SZovzLfjX"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="wIZNjA_0LgfN"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/7章') #ここを変更。

# %% [markdown] id="S0m3EV2sLevt"
# # 7章 ロジスティクスネットワークの最適設計を行う10本ノック
#
# ここでは、最適化計算を行ういくつかのライブラリを用いて、最適化計算を実際に行っていきます。  
# そして、前章で用いたネットワーク可視化などの技術を駆使し、計算結果の妥当性を確認する方法についても学んでいきます。

# %% [markdown] id="DlzzpnaZLevu"
# ### ノック６１：輸送最適化問題を解いてみよう

# %% id="gbSduWAsLevu"

# %% [markdown] id="7h6gYEX9Levv"
# ### ノック６２：最適輸送ルートをネットワークで確認しよう

# %% id="q15oafrwLevv"

# %% [markdown] id="HW_M4YaoLevv"
# ### ノック６３：最適輸送ルートが制約条件内に収まっているかどうかを確認しよう

# %% id="52IbGV40Levv"

# %% [markdown] id="m90MKWqfLevv"
# ### ノック６４：生産計画に関するデータを読み込んでみよう

# %% id="NESXuqc0Levv"

# %% [markdown] id="tA58Po-JLevw"
# ### ノック６５：利益を計算する関数を作ってみよう

# %% id="b-WbTaSvLevw"

# %% [markdown] id="SoKD6-0TLevw"
# ### ノック６６：生産最適化問題を解いてみよう

# %% id="soewz566Levw"

# %% [markdown] id="mBHVC4wFLevw"
# ### ノック６７：最適生産計画が制約条件内に収まっているかどうかを確認しよう

# %% id="g4N8fOmTLevw"

# %% [markdown] id="4Tt3n0_ILevw"
# ### ノック６８：ロジスティクスネットワーク設計問題を解いてみよう

# %% id="9ZL6E4fJLevw"

# %% [markdown] id="rosRiCd1Levx"
# ### ノック６９：最適ネットワークにおける輸送コストとその内訳を計算しよう

# %% id="dGLb0Sk2Levx"

# %% [markdown] id="QKL6ZJ13Levx"
# ### ノック７０：最適ネットワークにおける生産コストとその内訳を計算しよう

# %% id="pms3fFC-Levx"
