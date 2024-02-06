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

# %% id="IQIrkqe0LNZ6"
# Google Driveと接続を行います。これを行うことで、Driveにあるデータにアクセスできるようになります。
# 下記セルを実行すると、Googleアカウントのログインを求められますのでログインしてください。
from google.colab import drive
drive.mount('/content/drive')

# %% id="B-8veJEWLQKm"
# 作業フォルダへの移動を行います。
# 人によって作業場所がことなるので、その場合作業場所を変更してください。
import os 
os.chdir('/content/drive/MyDrive/100knock-data_analytics/6章') #ここを変更。

# %% [markdown] id="h9v6FjWpLMdo"
# # 6章 物流の最適ルートをコンサルティングする１０本ノック
#
# ここでは、「物流」の基礎となる「輸送最適化」を検討するにあたっての基礎的な技術を習得します。  
# 実際の物流データからネットワーク構造を可視化する方法について学び、最適な物流計画を立案する流れを学んでいきます。

# %% [markdown] id="i7xghZSSLMdr"
# ### ノック５１：物流に関するデータを読み込んでみよう

# %% id="n8BdTNYhLMdr"

# %% id="FPvDjDBWLMdr"

# %% id="ApQ7Wy9uLMdr"

# %% id="pRsC3K3gLMdr"

# %% id="BQnJWl8oLMdr"

# %% id="Fe42OBViLMdr"

# %% id="05DlTarCLMds"

# %% id="CoWYtp3nLMds"

# %% id="PCbZoyFSLMds"

# %% [markdown] id="B_bge5n3LMds"
# ### ノック５２：現状の輸送量、コストを確認してみよう

# %% id="X61_gmaqLMds"

# %% id="Nww_21UZLMds"

# %% id="GNaqWZavLMds"

# %% id="1hRxA3rTLMds"

# %% [markdown] id="XwR9X-ZMLMds"
# ### ノック５３：ネットワークを可視化してみよう

# %% id="HBP_WJAQLMdt"

# %% [markdown] id="wP3o-0QyLMdt"
# ### ノック５４：ネットワークにノードを追加してみよう

# %% id="Lybili2KLMdt"

# %% [markdown] id="fTuEQNG0LMdt"
# ### ノック５５：ルートの重みづけを実施しよう

# %% id="kwS4Oa16LMdt"

# %% [markdown] id="AqRPXXyCLMdt"
# ### ノック５６：輸送ルート情報を読み込んでみよう

# %% id="tpEHC9e8LMdt"

# %% [markdown] id="jK8b2lusLMdt"
# ### ノック５７：輸送ルート情報からネットワークを可視化してみよう

# %% id="AeIHWEhGLMdt"

# %% [markdown] id="biiZ5fADLMdt"
# ### ノック５８：輸送コスト関数を作成しよう

# %% id="7YrW-QwfLMdt"

# %% [markdown] id="ASwTMEWdLMdt"
# ### ノック５９：制約条件を作ってみよう

# %% id="DZSk7g5KLMdu"

# %% [markdown] id="gYnVM2AGLMdu"
# ### ノック６０：輸送ルートを変更して、輸送コスト関数の変化を確認しよう

# %% id="fACVkSy6LMdu"

# %% id="ARWVZfT1LMdu"
