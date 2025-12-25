import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sample_ Superstore.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df.head()
df.info()
df.describe()

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

category_sales.plot(kind='bar', title='Sales by Category')
plt.show()
region_profit = df.groupby('Region')['Profit'].sum().sort_values()

region_profit.plot(kind='barh', title='Profit by Region')
plt.show()
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()

monthly_sales = (
    df.set_index('Order Date').resample('M')['Sales'].sum()
)

monthly_sales.plot(title="Monthly Sales Trend")
plt.show()

forecast = monthly_sales.rolling(window=3).mean()

plt.plot(monthly_sales, label='Actual')
plt.plot(forecast, label='Forecast', linestyle='--')
plt.legend()
plt.show()
