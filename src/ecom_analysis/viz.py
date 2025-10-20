from matplotlib import pyplot as plt
import seaborn as sns

def plot_sales_over_time(sales_data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=sales_data, x='date', y='sales', marker='o')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_category_distribution(sales_data):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=sales_data, x='category', order=sales_data['category'].value_counts().index)
    plt.title('Sales Distribution by Category')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_top_n_products(sales_data, n=10):
    top_products = sales_data.groupby('product_name')['sales'].sum().nlargest(n).reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_products, x='sales', y='product_name', palette='viridis')
    plt.title(f'Top {n} Products by Sales')
    plt.xlabel('Sales')
    plt.ylabel('Product Name')
    plt.tight_layout()
    plt.show()