import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="Big Mart Sales Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    """Load and cache the Big Mart dataset"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'Big_Mart.csv')
    df = pd.read_csv(csv_path)
    
    column_mapping = {
        'ProductID': 'Item_Identifier',
        'Weight': 'Item_Weight',
        'FatContent': 'Item_Fat_Content',
        'ProductVisibility': 'Item_Visibility',
        'ProductType': 'Item_Type',
        'MRP': 'Item_MRP',
        'OutletID': 'Outlet_Identifier',
        'EstablishmentYear': 'Outlet_Establishment_Year',
        'OutletSize': 'Outlet_Size',
        'LocationType': 'Outlet_Location_Type',
        'OutletType': 'Outlet_Type',
        'OutletSales': 'Item_Outlet_Sales'
    }
    
    df = df.rename(columns=column_mapping)
    return df

# Load data
df = load_data()

# Header Section
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 0.5rem;'>Big Mart Sales Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666; margin-bottom: 2rem;'>Analysis and Prediction of the Big Mart Outlet Sales</h3>", unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.header("🔧 Filters")

# Product Type Filter
product_types = ['All'] + sorted(df['Item_Type'].unique().tolist())
selected_product_type = st.sidebar.selectbox(
    "Select Product Type:",
    options=product_types,
    index=0
)

# City Tier Filter
city_tiers = ['All'] + sorted(df['Outlet_Location_Type'].unique().tolist())
selected_city_tier = st.sidebar.selectbox(
    "Select City Tier:",
    options=city_tiers,
    index=0
)

# Store Category Filter
store_categories = ['All'] + sorted(df['Outlet_Type'].unique().tolist())
selected_store_category = st.sidebar.selectbox(
    "Select Store Category:",
    options=store_categories,
    index=0
)

# Apply filters to the dataframe
filtered_df = df.copy()

if selected_product_type != 'All':
    filtered_df = filtered_df[filtered_df['Item_Type'] == selected_product_type]

if selected_city_tier != 'All':
    filtered_df = filtered_df[filtered_df['Outlet_Location_Type'] == selected_city_tier]

if selected_store_category != 'All':
    filtered_df = filtered_df[filtered_df['Outlet_Type'] == selected_store_category]

data = filtered_df

# Key Metrics Overview
st.header("📊 Key Metrics Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_observations = len(data)
    st.metric("Total Observations", f"{total_observations:,}")
    
    product_types_count = data['Item_Type'].nunique()
    st.metric("Product Types", product_types_count)

with col2:
    if len(data) > 0:
        highest_mrp = data['Item_MRP'].max()
        st.metric("Highest MRP", f"${highest_mrp:,.2f}")
        
        min_year = data['Outlet_Establishment_Year'].min()
        max_year = data['Outlet_Establishment_Year'].max()
        st.metric("Establishment Years", f"{min_year} - {max_year}")
    else:
        st.metric("Highest MRP", "No data")
        st.metric("Establishment Years", "No data")

with col3:
    if len(data) > 0:
        avg_store_sales = data['Item_Outlet_Sales'].mean()
        st.metric("Average Store Sales", f"${avg_store_sales:,.2f}")
        
        total_store_sales = data['Item_Outlet_Sales'].sum()
        st.metric("Total Store Sales", f"${total_store_sales:,.2f}")
    else:
        st.metric("Average Store Sales", "No data")
        st.metric("Total Store Sales", "No data")

with col4:
    if len(data) > 0:
        avg_mrp = data['Item_MRP'].mean()
        st.metric("Average MRP", f"${avg_mrp:,.2f}")
    else:
        st.metric("Average MRP", "No data")

# Missing Values Analysis
st.header("🔍 Missing Values Analysis")

missing_data = []
for col in ['Item_Weight', 'Outlet_Size']:
    missing_count = data[col].isnull().sum()
    missing_percentage = (missing_count / len(data)) * 100 if len(data) > 0 else 0
    missing_data.append({
        'Column': col,
        'Missing Values': missing_count,
        'Percentage (%)': round(missing_percentage, 2)
    })

missing_df = pd.DataFrame(missing_data)
st.dataframe(missing_df, width="stretch")

# Data Visualization Section
st.header("📈 Visualizations")

if len(data) == 0:
    st.warning("⚠️ No data available for the selected filters. Please adjust your filter selection.")
else:
    vis_col1, vis_col2 = st.columns(2)

    with vis_col1:
        # Store Sales vs. MRP
        st.subheader("Store Sales vs. MRP")
        fig_scatter = px.scatter(
            data, 
            x='Item_MRP', 
            y='Item_Outlet_Sales',
            color='Outlet_Type',
            title="Relationship between Item MRP and Outlet Sales",
            labels={'Item_MRP': 'Item MRP ($)', 'Item_Outlet_Sales': 'Item Outlet Sales ($)'},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_scatter, width="stretch")
        
        # Store Size Distribution
        st.subheader("Store Size Distribution")
        df_size = data.copy()
        df_size['Outlet_Size'] = df_size['Outlet_Size'].fillna('Unknown')
        size_counts = df_size['Outlet_Size'].value_counts()
        if len(size_counts) > 0:
            fig_pie_size = px.pie(
                values=size_counts.values,
                names=size_counts.index,
                title="Distribution of Outlet Sizes"
            )
            st.plotly_chart(fig_pie_size, width="stretch")
        else:
            st.info("No data available for this visualization")
        
        # City Tier Distribution
        st.subheader("City Tier Distribution")
        tier_counts = data['Outlet_Location_Type'].value_counts()
        if len(tier_counts) > 0:
            fig_bar_tier = px.bar(
                x=tier_counts.index,
                y=tier_counts.values,
                title="Count by Outlet Location Type",
                labels={'x': 'Outlet Location Type', 'y': 'Count'},
                color=tier_counts.index,
                color_discrete_sequence=px.colors.qualitative.Pastel1
            )
            st.plotly_chart(fig_bar_tier, width="stretch")
        else:
            st.info("No data available for this visualization")
        
        # Average Sales by Store Category
        st.subheader("Average Sales by Store Category")
        avg_sales_by_type = data.groupby('Outlet_Type')['Item_Outlet_Sales'].mean().reset_index()
        if len(avg_sales_by_type) > 0:
            fig_bar_avg = px.bar(
                avg_sales_by_type,
                x='Outlet_Type',
                y='Item_Outlet_Sales',
                title="Average Item Outlet Sales by Outlet Type",
                labels={'Outlet_Type': 'Outlet Type', 'Item_Outlet_Sales': 'Average Sales ($)'},
                color='Outlet_Type',
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig_bar_avg, width="stretch")
        else:
            st.info("No data available for this visualization")

    with vis_col2:
        # Store Sales Distribution
        st.subheader("Store Sales Distribution")
        fig_hist_sales = px.histogram(
            data,
            x='Item_Outlet_Sales',
            title="Distribution of Item Outlet Sales",
            labels={'Item_Outlet_Sales': 'Item Outlet Sales ($)', 'count': 'Frequency'},
            nbins=50
        )
        st.plotly_chart(fig_hist_sales, width="stretch")
        
        # Product Visibility Distribution
        st.subheader("Product Visibility Distribution")
        fig_hist_visibility = px.histogram(
            data,
            x='Item_Visibility',
            title="Distribution of Item Visibility",
            labels={'Item_Visibility': 'Item Visibility', 'count': 'Frequency'},
            nbins=50
        )
        st.plotly_chart(fig_hist_visibility, width="stretch")
        
        # Total Sales by Fat Content
        st.subheader("Total Sales by Fat Content")
        # Standardize fat content values
        fat_content_df = data.copy()
        fat_content_df['Item_Fat_Content'] = fat_content_df['Item_Fat_Content'].replace({
            'LF': 'Low Fat',
            'low fat': 'Low Fat',
            'reg': 'Regular'
        })
        
        fat_sales = fat_content_df.groupby('Item_Fat_Content')['Item_Outlet_Sales'].sum().reset_index()
        if len(fat_sales) > 0:
            fig_bar_fat = px.bar(
                fat_sales,
                x='Item_Fat_Content',
                y='Item_Outlet_Sales',
                title="Total Item Outlet Sales by Fat Content",
                labels={'Item_Fat_Content': 'Item Fat Content', 'Item_Outlet_Sales': 'Total Sales ($)'},
                color='Item_Fat_Content',
                color_discrete_sequence=px.colors.qualitative.Bold
            )
            st.plotly_chart(fig_bar_fat, width="stretch")
        else:
            st.info("No data available for this visualization")
        
        # Total Sales by City Tier
        st.subheader("Total Sales by City Tier")
        tier_sales = data.groupby('Outlet_Location_Type')['Item_Outlet_Sales'].sum().reset_index()
        if len(tier_sales) > 0:
            fig_bar_tier_sales = px.bar(
                tier_sales,
                x='Outlet_Location_Type',
                y='Item_Outlet_Sales',
                title="Total Item Outlet Sales by City Tier",
                labels={'Outlet_Location_Type': 'Outlet Location Type', 'Item_Outlet_Sales': 'Total Sales ($)'},
                color='Outlet_Location_Type',
                color_discrete_sequence=px.colors.qualitative.Vivid
            )
            st.plotly_chart(fig_bar_tier_sales, width="stretch")
        else:
            st.info("No data available for this visualization")

    # Total Sales by Product Type - Full width
    st.subheader("Total Sales by Product Type")
    type_sales_total = data.groupby('Item_Type')['Item_Outlet_Sales'].sum().reset_index()
    if len(type_sales_total) > 0:
        type_sales_total = type_sales_total.sort_values('Item_Outlet_Sales', ascending=False)
        
        fig_bar_product_total = px.bar(
            type_sales_total,
            x='Item_Type',
            y='Item_Outlet_Sales',
            title="Total Sales Amount by Product Type",
            labels={'Item_Type': 'Product Type', 'Item_Outlet_Sales': 'Total Sales ($)'},
            color='Item_Type',
            color_discrete_sequence=px.colors.qualitative.Dark24
        )
        fig_bar_product_total.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar_product_total, width="stretch")
    else:
        st.info("No data available for this visualization")

    # Sales by Product Type (%)
    st.subheader("Sales by Product Type (%)")
    type_sales = data.groupby('Item_Type')['Item_Outlet_Sales'].sum().reset_index()
    if len(type_sales) > 0:
        fig_pie_type = px.pie(
            values=type_sales['Item_Outlet_Sales'].values,
            names=type_sales['Item_Type'].values,
            title="Percentage of Total Sales by Product Type"
        )
        st.plotly_chart(fig_pie_type, width="stretch")
    else:
        st.info("No data available for this visualization")

# Advanced Analytics Section
st.header("🔍 Advanced Analytics")

if len(data) > 0:
    adv_col1, adv_col2 = st.columns(2)
    
    with adv_col1:
        # Sales Performance by Store Age
        st.subheader("Sales Trends by Store Age")
        current_year = 2025 
        store_age_df = data.copy()
        store_age_df['Store_Age'] = current_year - store_age_df['Outlet_Establishment_Year']
        age_sales = store_age_df.groupby('Store_Age')['Item_Outlet_Sales'].mean().reset_index()
        age_sales = age_sales.sort_values('Store_Age')
        
        fig_line_age = px.line(
            age_sales,
            x='Store_Age',
            y='Item_Outlet_Sales',
            title="Average Sales vs Store Age",
            labels={'Store_Age': 'Store Age (Years)', 'Item_Outlet_Sales': 'Average Sales ($)'},
            markers=True
        )
        fig_line_age.update_traces(line=dict(color='#1f77b4', width=3))
        st.plotly_chart(fig_line_age, width="stretch")
        
    with adv_col2:
        # Sales Distribution by Outlet Type
        st.subheader("Sales Distribution by Store Type")
        fig_box = px.box(
            data,
            x='Outlet_Type',
            y='Item_Outlet_Sales',
            title="Sales Distribution Analysis by Store Type",
            labels={'Outlet_Type': 'Store Type', 'Item_Outlet_Sales': 'Sales ($)'},
            color='Outlet_Type',
            color_discrete_sequence=px.colors.qualitative.Pastel2
        )
        fig_box.update_layout(xaxis_tickangle=-30)
        st.plotly_chart(fig_box, width="stretch")
    
    st.subheader("Product Performance Matrix")
    bubble_data = data.groupby('Item_Type').agg({
        'Item_MRP': 'mean',
        'Item_Visibility': 'mean', 
        'Item_Outlet_Sales': ['mean', 'count']
    }).round(2)
    
    bubble_data.columns = ['Avg_MRP', 'Avg_Visibility', 'Avg_Sales', 'Product_Count']
    bubble_data = bubble_data.reset_index()
    
    fig_bubble = px.scatter(
        bubble_data,
        x='Avg_MRP',
        y='Avg_Sales',
        size='Product_Count',
        color='Avg_Visibility',
        hover_name='Item_Type',
        title="Product Performance Matrix: Price vs Sales (Size = Volume, Color = Visibility)",
        labels={
            'Avg_MRP': 'Average Price ($)',
            'Avg_Sales': 'Average Sales ($)',
            'Avg_Visibility': 'Avg Visibility'
        },
        color_continuous_scale='plasma',
        size_max=50
    )
    st.plotly_chart(fig_bubble, width="stretch")

else:
    st.warning("⚠️ No data available for advanced analytics.")

# Key Business Insights
st.header("💡 Key Business Insights")

insights_col1, insights_col2 = st.columns(2)

with insights_col1:
    st.markdown("""
    **Product Performance:**
    - Fruits, Vegetables, and Snack Foods account for the highest sales, making up nearly 30% of total products.
    
    **Fat Content Impact:**
    - Low Fat products sell significantly more than Regular ones.
    
    **Pricing Strategy:**
    - Sales are strongly influenced by MRP (Maximum Retail Price).
    """)

with insights_col2:
    st.markdown("""
    **Store Performance:**
    - Grocery stores have the lowest average sales, while Supermarket Type 3 records the highest.
    
    **Product Visibility:**
    - There is no clear relationship between product visibility and sales, as the data does not provide strong evidence.
    """)

# Model Summary Section
st.header("🔬 Model Performance Summary")

# Key metrics in columns
metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric("R-squared", "0.553")

with metric_col2:
    st.metric("Adj. R-squared", "0.552")

with metric_col3:
    st.metric("F-statistic", "424.8")

# Full model details
with st.expander("Click to see full model details"):
    st.text("""
==============================================================================
Dep. Variable:             StoreSales   R-squared:                       0.553
Model:                            OLS   Adj. R-squared:                  0.552
Method:                 Least Squares   F-statistic:                     424.8
Date:                Sat, 20 Sep 2025   Prob (F-statistic):               0.00
Time:                        17:41:10   Log-Likelihood:                -54402.
No. Observations:                6532   AIC:                         1.088e+05
Df Residuals:                    6512   BIC:                         1.090e+05
Df Model:                          19
Covariance Type:            nonrobust
==============================================================================
    """)

st.markdown("---")
st.markdown("*The Dashboard Was Created By One Of The Sons Of The Historic Sudair Region*")
