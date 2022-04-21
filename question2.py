grocery.groupby("product_description")["price"].apply(
    lambda x: x.max() - x.min()
)
max_apple = grocery[grocery.product_description=="apple"]["price"].max()
min_apple = grocery[grocery.product_description=="apple"]["price"].min()
max_apple - min_apple