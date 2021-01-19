#%%
import numpy as np
import pandas as pd


#%%
# And a partridge in a pear tree.# Two turtle doves,# Three French hens,# four calling birds# five gold rings# six geese a-laying# seven swans a-swimming# eight maids a-milking# nine ladies dancing# ten lords a-leaping# eleven pipers piping# twelve drummers drumming
startbag = [
    "partridge in a pear tree",
    "Two turtle doves",
    "Three French hens",
    "four calling birds",
    "five gold rings",
    "six geese a-laying",
    "seven swans a-swimming",
    "eight maids a-milking",
    "nine ladies dancing",
    "ten lords a-leaping",
    "eleven pipers piping",
    "twelve drummers drumming",
]
#%%
bag = []
i = 1
for x in startbag:
    for z in np.arange(i):
        bag.append(x)
    i += 1
original_bag = bag
# %%
def check_bag(bag, startbag):
    x = 0
    for item in startbag[1:]:
        new_count = bag.count(item)

        if x <= new_count:
            x = new_count
    return x


# %%
seed = 887234809
# %%
np.random.seed(seed)
num = []
#%%
for x in range(200000000):
    np.random.shuffle(bag)
    idx = bag.index(startbag[0])
    new_num = check_bag(bag[:idx], startbag)
    num.append(new_num)
print(f"done {len(num)}")
# %%
num_arr = np.array(num)
num_arr.mean()

# %%
# orig 6.858887333333334#
# 500k = 6.8576882
# 1m 6.858937
# 14m 6.859067785714286
# 24m 6.859931583333333
# 74m 6.859895 405405405
# 94m 6.859885 914893617
# 100m 6.85990 199 & 6.85961 363
# 200m 6.85964 3675
# 300m 6.85974 0413333333
# 500m


# %%
