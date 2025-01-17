import streamlit as st
import plotly.express as px 
import pandas as pd
df=pd.read_csv('alldf.csv')
st.set_page_config(page_title="My sale Dashboard",page_icon=":bar_chart:",layout="wide")
st.sidebar.header('Please Filter Here')
product_name=st.sidebar.multiselect("Select Product",
                       options=df['Product'].unique(),
                       default=df['Product'].unique()[:5])
city_name=st.sidebar.multiselect("Select City",
                       options=df['City'].unique(),
                       default=df['City'].unique()[:5])
month_name=st.sidebar.multiselect("Select Month",
                       options=df['Month'].unique(),
                       default=df['Month'].unique()[:5])
st.title(":bar_chart: Sale Dashboard")
st.markdown('##')
total=df['Total'].sum()
numOfProduct=df['Product'].nunique()
left_col , right_col=st.columns(2)
with left_col:
    st.subheader('Total Sale')
    st.subheader(f"US ${total}")
with right_col:
    st.subheader('No. of Product')
    st.subheader(f"{numOfProduct}")
df_select=df.query("City==@city_name and Product==@product_name and Month==@month_name")
aa=df_select.groupby('Product')['Total'].sum().sort_values()
figSaleByProduct=px.bar(
    aa,
    x=aa.values,
    y=aa.index,
    title='Total Sale by Product',
)
a , b , c =st.columns(3)
a.plotly_chart(figSaleByProduct,use_container_width=True)

bb=df_select.groupby('Month')['Total'].sum().sort_values()
figSaleByMonth=px.bar(
    bb,
    x=bb.values,
    y=bb.index,
    title='Total Sale by Month',
)
c.plotly_chart(figSaleByMonth,use_container_width=True)

figSaleByCity=px.pie(
    df_select,
    values='Total',
    names='City',
    title='Total Sale by City',
)
b.plotly_chart(figSaleByCity,use_container_width=True)

d,e=st.columns(2)
dd=df_select.groupby('Month')['Total'].sum().sort_values()
lineFigSaleByMonth=px.line(
    dd,
    x=dd.values,
    y=dd.index,
    title='Total Sale by Month',
)
d.plotly_chart(lineFigSaleByMonth,use_container_width=True)

scatterFigSaleByQuantity=px.scatter(
    df_select,
    x='Total',
    y='Quantity Ordered',
    title='Total Sale by Quantity',
)
e.plotly_chart(scatterFigSaleByQuantity,use_container_width=True)