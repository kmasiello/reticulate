# Py_hello
test = "Py hello"

# %pip install pandas
# %env RETICULATE_PYTHON


import pandas as pd 
netflix = pd.read_csv("https://raw.githubusercontent.com/practiceprobs/datasets/main/netflix-titles/netflix-titles.csv")
netflix.head()



