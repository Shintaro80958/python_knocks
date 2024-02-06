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

# %% id="8sSCfGshJtnq"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="IjX18iQTJv-O"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/2章') #ここを変更。

# %% [markdown] id="jUPbF5ydJqI9"
# # ２章　小売店のデータでデータ加工を行う１０本ノック
#
# 本章では、ある小売店の売上履歴と顧客台帳データを用いて、データ分析の素地となる「データの加工」を習得することが目的です。
# 実際の現場データは手入力のExcel等、決して綺麗なデータではない事が多いため、
# データの揺れや整合性の担保など、汚いデータを取り扱うデータ加工を主体に進めて行きます。

# %% [markdown] id="M_fjIZLNJqI-"
# ### ノック１１：データを読み込んでみよう

# %% id="OCu_vjQ3JqI_"

# %% id="wvwN80iHJqI_"

# %% [markdown] id="b_dHHOu-JqI_"
# ### ノック１２：データの揺れを見てみよう

# %% id="mEwhyMlJJqI_"

# %% id="5A9UIneJJqI_"

# %% id="stFBDxemJqI_"

# %% [markdown] id="1a4SLEh1JqJA"
# ### ノック１３：データに揺れがあるまま集計しよう

# %% id="AcNvgnkgJqJA"

# %% id="vXg8Vf7FJqJA"

# %% [markdown] id="YhOVk872JqJA"
# ### ノック１４：商品名の揺れを補正しよう

# %% id="iiRtJZ_6JqJA"

# %% id="oDsDXdP7JqJA"

# %% id="550d4UTRJqJA"

# %% [markdown] id="A_Cq9uv1JqJA"
# ### ノック１５：金額欠損値の補完をしよう

# %% id="LzrWu4MIJqJB"

# %% id="skbmk_T1JqJB"

# %% id="fHXKUybZJqJB"

# %% id="drS0Jw-IJqJB"

# %% [markdown] id="B4u8jL65JqJB"
# ### ノック１６：顧客名の揺れを補正しよう

# %% id="9_AhHz8vJqJB"

# %% id="MAlCTzx-JqJB"

# %% id="ElE8X_K3JqJB"

# %% [markdown] id="R_Dbo1v4JqJB"
# ### ノック１７：日付の揺れを補正しよう

# %% id="k96AaNrYJqJB"

# %% id="17vxIvtEJqJB"

# %% id="FkRzy0crJqJB"

# %% id="5ihENm0lJqJC"

# %% id="QrDzBs63JqJC"

# %% id="UB1eWbHoJqJC"

# %% [markdown] id="o_Gp-rmlJqJC"
# ### ノック１８：顧客名をキーに２つのデータを結合(ジョイン)しよう

# %% id="pv295MA3JqJC"

# %% [markdown] id="jW5S8iEWJqJC"
# ### ノック１９：クレンジングしたデータをダンプしよう

# %% id="fgNrz6rFJqJC"

# %% id="aFFFvXk5JqJC"

# %% [markdown] id="f2AmRZhjJqJC"
# ### ノック２０：データを集計しよう

# %% id="ka3FwyIkJqJC"

# %% id="nGzAf64lJqJC"

# %% id="osoHDU82JqJC"

# %% id="M8e7-VxQJqJC"

# %% id="You9a9egJqJC"

# %% id="08SYBvu3JqJD"
