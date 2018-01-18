from collections import Counter
import pandas as pd
import numpy as np

with open('data.txt', 'r') as f:
    res = f.readlines()

res = [x.split(" ") for x in [y.strip() for y in res]]

flattened_res = [item for sublist in res for item in sublist]

# print(flattened_res)

word_count = Counter(flattened_res)

# word_count_array = [(word, count) for (word, count) in word_count]

print(word_count)
# cleansed_list = []

# series = pd.Series(flattened_res)

# df = pd.DataFrame(word_count_array)
#
# # word_counts = series.value_counts()
#
# print(df)
# #
# # for x in word_counts:
# #     print(type(word_counts))
# #     print(type(x))
# #     print(x)
#
# # print(word_counts)
#
# for word, count in df:
#     print(word, count)