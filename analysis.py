import pandas as pd

# Load data
df = pd.read_csv("data/mobile.csv")

# Preview
print(df.head())



brand_rating = df.groupby("brand")["rating"].mean().sort_values(ascending=False)
print(brand_rating)


import matplotlib.pyplot as plt

plt.scatter(df["price"], df["rating"])
plt.xlabel("Price")
plt.ylabel("Rating")
plt.title("Price vs Rating")
plt.show()



top_phones = df.sort_values(by="reviews_count", ascending=False).head(10)
print(top_phones)



def price_category(price):
    if price < 10000:
        return "Budget"
    elif price < 20000:
        return "Mid-range"
    else:
        return "Premium"

df["price_category"] = df["price"].apply(price_category)