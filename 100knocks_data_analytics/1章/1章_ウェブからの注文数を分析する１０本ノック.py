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

# %% [markdown] id="qUQ5OkKmJ1mJ"
# # １章 ウェブの注文数を分析する１０本ノック
#
# ここでは、ある企業のECサイトでの商品の注文数の推移を分析していきます。  
# データの属性を理解し、分析をするためにデータを加工した後、  
# データの可視化を行うことで問題を発見していくプロセスを学びます。

# %% [markdown] id="HyMoAlu5J1mN"
# ### ノック１：データを読み込んでみよう

# %% id="Wicqn13lJ1mO"
import pandas as pd

# %%
transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
transaction_detail_2.head()

# %%
transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
transaction_detail_1.head()

# %%
transaction_2 = pd.read_csv('transaction_2.csv')
transaction_2.head()

# %%
transaction_1 = pd.read_csv('transaction_1.csv')
transaction_1.head()

# %%
item_master = pd.read_csv('item_master.csv')
item_master.head()

# %%
customer_master = pd.read_csv('customer_master.csv')
customer_master.head()

# %% id="rJm5rP2uJ1mP"

# %% id="iPazmB_tJ1mP"

# %% id="13Byx1zPJ1mQ"

# %% [markdown] id="tUj49Lq2J1mQ"
# ### ノック２：データを結合(ユニオン)してみよう

# %% id="yToHeaCkJ1mR"
transaction = pd.concat([transaction_1, transaction_2])
# print(len(transaction_1))
# print(len(transaction_2))
# print(len(transaction))
transaction.head()

# %% id="nIlKzMwUJ1mS"
transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2])
# print(len(transaction_detail_1))
# print(len(transaction_detail_2))
# print(len(transaction_detail))
transaction_detail.head()

# %% id="UI1QoncnJ1mS"

# %% [markdown] id="hL_2eEJsJ1mS"
# ### ノック３：売上データ同士を結合(ジョイン)してみよう

# %% id="cM5Iq_32J1mT"
# ミス
pd.merge(transaction, transaction_detail, on='transaction_id')

# %% id="dEIa14ICJ1mT"
join_data = pd.merge(transaction_detail, transaction[['transaction_id', 'customer_id', 'payment_date']], on='transaction_id', how='left')
join_data.head()

# %%
print(len(transaction))
print(len(transaction_detail))
print(len(join_data))

# %% [markdown] id="N68ukZAbJ1mT"
# ### ノック４：マスタデータを結合(ジョイン)してみよう

# %% id="jAi74QxfJ1mT"
join_data = pd.merge(join_data, item_master, on='item_id', how='left')
join_data = pd.merge(join_data, customer_master, on='customer_id', how='left')
join_data.head()

# %%

# %% [markdown] id="PC6cvtpvJ1mT"
# ### ノック5：必要なデータ列を作ろう

# %% id="7oTFxMNsJ1mU"
join_data['price'] = join_data['quantity'] * join_data['item_price']
join_data[['price', 'quantity', 'item_price']].head()

# %% [markdown] id="9_CDTQ9OJ1mU"
# ### ノック6：データ検算をしよう

# %% id="F7hNI74PJ1mU"
print(join_data['price'].sum())
print(transaction['price'].sum())

# %% id="hP3vtiFGJ1mU"

# %% [markdown] id="SUIoReEXJ1mU"
# ### ノック7：各種統計量を把握しよう

# %% id="ybIheNP9J1mV"
join_data.isnull().sum()

# %% id="XeY8QOZ0J1mV"
join_data.describe()

# %% id="WvF_-kmuJ1mV"
print(join_data['payment_date'].min())
print(join_data['payment_date'].max())

# %% [markdown] id="IWYKOREPJ1mV"
# ### ノック8：月別でデータを集計してみよう

# %% id="s3ljKRbsJ1mV"
join_data.dtypes

# %% id="gFaE0moTJ1mV"
join_data['payment_date'] = pd.to_datetime(join_data['payment_date'])
join_data['payment_month'] = join_data['payment_date'].dt.strftime('%Y%m')

# %% id="e1VQDr9dJ1mV"
join_data.head()

# %% [markdown] id="NEsEIEtWJ1mV"
# ### ノック9：月別、商品別でデータを集計してみよう

# %% id="aZyzr_vIJ1mW"
join_data.groupby('payment_month')['price'].sum()

# %% id="L2zR-vGTJ1mW"
join_data.groupby(['payment_month', 'item_name'])[['quantity', 'price']].sum()

# %% [markdown]
#

# %%
pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price', 'quantity'], aggfunc='sum')

# %% [markdown] id="7RXaPfePJ1mW"
# ### ノック10：商品別の売上推移を可視化してみよう

# %% id="JG1yWhO7J1mW"
graph_data = pd.pivot_table(join_data, index='payment_month', columns='item_name', values='price', aggfunc='sum')
graph_data.head()

# %% id="NWudJq7YJ1mW"
import matplotlib.pyplot as plt

# %% id="xeQcyLAXJ1mW"
plt.plot(list(graph_data.index), graph_data['PC-A'], label='PC-A')
plt.plot(list(graph_data.index), graph_data['PC-B'], label='PC-B')
plt.plot(list(graph_data.index), graph_data['PC-C'], label='PC-C')
plt.plot(list(graph_data.index), graph_data['PC-D'], label='PC-D')
plt.plot(list(graph_data.index), graph_data['PC-E'], label='PC-E')
plt.legend()

# %%
