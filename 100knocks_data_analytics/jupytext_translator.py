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

# %%
import os
import jupytext

# %%
current_directory = os.getcwd()

# %%
for dirpath, dirnames, filenames in os.walk(current_directory):
    for filename in filenames:
        if filename.endswith(".ipynb"):
            notebook_path = os.path.join(dirpath, filename)
            notebook = jupytext.read(notebook_path)
            py_path = notebook_path.replace('.ipynb', '.py')
            jupytext.write(notebook, py_path, fmt='py:percent')

# %%

# %%
