import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Data/MatPlotLib-Data/sales.csv')
# print(data.head())

## opg. 1

plt.figure(figsize=(10, 6))
plt.plot(
    data["month_number"],
    data["total_profit"],
    marker='o',
    linestyle='-',
    color='b',
    label="total profit",
)

plt.title("total profit per month")
plt.xlabel("month")
plt.ylabel("total profit")
plt.xticks(data["month_number"])
plt.grid(True)
plt.legend()
plt.show()


## opg. 2

plt.figure(figsize=(10, 6))
for col in data:
    if col == "month_number" or col == "total_units" or col == "total_profit":
        continue
    plt.plot(
        data["month_number"],
        data[col],
        marker='o',
        linestyle='-',
        label=col,
    )
plt.title("sales per month")
plt.xlabel("month")
plt.ylabel("product")
plt.xticks(data["month_number"])
plt.grid(True)
plt.legend()
plt.show()


## opg. 3

products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
total_sales = dict((product, data[product].sum()) for product in products)

plt.figure(figsize=(8, 8))
plt.pie(
    [*total_sales.values()],
    labels=[*total_sales.keys()],
)
plt.axis("equal")
plt.show()

## opg. 4

products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
months = data["month_number"]
product_data = dict((key, data[key]) for key in products)
plt.figure(figsize=(12, 8))
plt.stackplot(months, *product_data.values(), labels=product_data.keys())
plt.xticks(months)
plt.legend()
plt.show()


