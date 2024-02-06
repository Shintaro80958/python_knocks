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

# %% id="T9FPIUOCKI0d"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="IMxyyuaYKK8u"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/3章') #ここを変更。

# %% [markdown] id="XUcD3f8uKILx"
# # 3章 顧客の全体像を把握する１０本ノック
#
# ここでは、スポーツジムの会員データを使って顧客の行動を分析していきます。  
# これまでと同様にまずはデータを理解し、加工した後、  
# 顧客の行動データを分析していきましょう。  
# ここでは、機械学習に向けての初期分析を行います。

# %% [markdown] id="07fglpCTKILy"
# ### ノック21：データを読み込んで把握しよう

# %% id="oFM-X01lKILz"

# %% id="OXYBY9_pKILz"

# %% id="MeSL9bPJKILz"

# %% id="pHOluPf5KILz"

# %% [markdown] id="anX-x1nHKILz"
# ### ノック22：顧客データを整形しよう

# %% id="T5dxua0dKIL0"

# %% id="vvT6g_iJKIL0"

# %% id="HTwLU3whKIL0"

# %% [markdown] id="dzblXI71KIL0"
# ### ノック23：顧客データの基礎集計をしよう

# %% id="WX7cFhpXKIL0"

# %% id="xDn9frs4KIL0"

# %% id="w5-aQUVNKIL0"

# %% id="pag-uaX6KIL0"

# %% id="8qZms8w_KIL0"

# %% [markdown] id="Qjo_a3euKIL1"
# ### ノック24：最新顧客データの基礎集計をしよう

# %% id="6Q_JD3yyKIL1"

# %% id="pKbTAK6AKIL1"

# %% id="oAQGAz_wKIL1"

# %% id="-VYiSBkdKIL1"

# %% [markdown] id="xRmE4zlwKIL1"
# ### ノック25：利用履歴データを集計しよう

# %% id="1BrWqa5GKIL1"

# %% id="4W-OWQAwKIL1"

# %% [markdown] id="wR4UDwQ2KIL1"
# ### ノック26：利用履歴データから定期利用フラグを作成しよう

# %% id="uxwi8lZhKIL1"

# %% id="787LY4C7KIL1"

# %% [markdown] id="GMfOWq4wKIL1"
# ### ノック27：顧客データと利用履歴データを結合しよう

# %% id="Zz9o_A5TKIL2"

# %% id="KOMpeH-jKIL2"

# %% [markdown] id="sn4IBFo7KIL2"
# ### ノック28：会員期間を計算しよう

# %% id="RRT2n_jIKIL2"

# %% [markdown] id="r9PavBhjKIL2"
# ### ノック29：顧客行動の各種統計量を把握しよう

# %% id="zAI3JiomKIL2"

# %% id="H1tmm8GXKIL2"

# %% id="IpU0bCisKIL2"

# %% [markdown] id="XSzfkNXMKIL2"
# ### ノック30：退会ユーザーと継続ユーザーの違いを把握しよう

# %% id="qATiI7a8KIL2"

# %% id="KYzKwxWWKIL2"

# %% id="hAuxrSD3KIL2"
