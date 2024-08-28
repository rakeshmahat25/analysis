import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("sales_advertising.csv")

# Set the title of the app
st.title("Data Display in Streamlit")

# Display the DataFrame
st.write("Here is the DataFrame:")
# st.dataframe(df.head())
st.dataframe(df.head(), width=1200, height=400)


# st.dataframe(df.columns)

df_columns_as_rows = pd.DataFrame(df.columns, columns=["Column Names"])

# Display the DataFrame
st.dataframe(df_columns_as_rows)

st.title("The total shape of the Data")
st.dataframe(df.shape)

st.title("Checking the total null values in the DataSet")
st.dataframe(df.isna().sum())


st.title("Removing all the rows having all values values")

clean_df = df.dropna(how='all')
clean_df.reset_index(drop=True, inplace=True)
clean_df.index = clean_df.index + 1
st.dataframe(clean_df)

Adata = pd.read_csv("short_data.csv")
st.dataframe(clean_df.describe())


st.write("Visualization of Product with histogram")
plt.figure(figsize=(30,14))
# sns.histplot(clean_df["Product Name"],bins=(1,100,7))
sns.histplot(Adata["Product Name"], discrete=True, bins=len(Adata["Product Name"].unique()), color='red')

plt.title("Product Sales", loc = 'center')
plt.xlabel("Name of Product ")
plt.ylabel("Sales Quantity")
plt.xticks(rotation='vertical')

st.pyplot(plt)


# st.markdown("<h3 style='color: red;'>Sales of the Product according to color</h3>", unsafe_allow_html=True)
# product_name = 'Sleek Earbuds'
# filtered_data = Adata[Adata['Product Name'] == product_name]
# data_aggregated = filtered_data.groupby('Product Colour').size().reset_index(name='Count')
# data_aggregated['Label'] = data_aggregated['Product Colour']
# colors =['#111000','#FF0000','#00FFFF','#FFFFF1']

# plt.figure(figsize=(15,8))
# plt.bar(data_aggregated['Count'],Adata['Product Name'].count(), labels=data_aggregated['Label'], autopct='%1.1f%%', colors=colors)

# st.pyplot(plt)


# plt.figure(figsize=(30,12))
# x = Adata["Product Name"]
z = Adata["Final Amount"]

# plt.xlabel("Date")
# plt.ylabel("Product with amount")
# # plt.scatter(x,z)

# st.pyplot(plt)


mean1 = z.mean()
st.write(f"The average order amount of the Order is {mean1:.2f}")




Adata['Time'] = pd.to_datetime(Adata['Time'])
unique_times_sorted = Adata['Time'].drop_duplicates().sort_values().reset_index(drop=True)

for target_date in unique_times_sorted:
    
    filtered_df = Adata[Adata['Time'] == target_date]
    row_count = filtered_df.shape[0]
    st.write(f"The total order of {target_date} is {row_count}")


st.write(f" ")


st.title("Barplot of Daily Sales")
order_counts = Adata['Time'].value_counts().sort_index()

plt.figure(figsize =(20,15))
plt.bar(order_counts.index, order_counts.values, color='green')
plt.title("Daily Sales", loc = 'center')
plt.xlabel("Date ")
plt.ylabel("Sales Quantity")
plt.xticks(rotation='vertical')



for date, count in order_counts.items():
    plt.text(date, count + 1, str(count), ha='center', va='bottom', rotation=0, fontsize=10)

st.pyplot(plt)

st.title("Histplot of Final Amount")

plt.figure(figsize=(30,15))
sns.histplot(Adata['Final Amount'],kde=True)
st.pyplot(plt)