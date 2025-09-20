# 🏪 Big Mart Sales Analytics Dashboard
A comprehensive Streamlit dashboard for analyzing Big Mart outlet sales data with interactive visualizations, advanced analytics, and business insights.

## 📊 Features

### 📈 Key Metrics Overview
**Key Performance Indicators (KPIs)**
- Total observations count
- Product types diversity
- Highest MRP tracking
- Establishment years range
- Average and total store sales
- Average MRP analysis

**Interactive Charts**
- Store sales vs. MRP relationship
- Store size distribution
- City tier performance
- Sales by store category

### 🔍 Data Analysis Dashboard
**Missing Values Analysis**
- Item weight missing data tracking
- Outlet size data completeness
- Percentage-based missing value insights

**Product Performance**
- Sales distribution patterns
- Product visibility analysis
- Fat content sales comparison
- Product type revenue breakdown

### 💰 Revenue Analytics
**Sales by Categories**
- Total sales by product type
- Fat content performance comparison
- City tier revenue analysis
- Store category profitability

**Advanced Analytics**
- Sales trends by store age
- Sales distribution by store type
- Product performance matrix (multi-dimensional)

### 🔍 Interactive Filters
**Product Type Filter**: Select specific product categories for analysis
**City Tier Filter**: Filter data by location tiers (Tier 1, 2, 3)
**Store Category Filter**: Analyze by store types (Grocery, Supermarket Types)
- Real-time data filtering across all visualizations

### 💡 Business Insights
**Key Findings**
- Fruits, Vegetables, and Snack Foods performance insights
- Low Fat vs Regular product sales analysis
- MRP influence on sales patterns
- Store type performance benchmarking
- Product visibility impact assessment

### 🔬 Model Performance
**OLS Regression Model Summary**
- R-squared: 0.553
- Adjusted R-squared: 0.552
- F-statistic: 424.8
- Complete model statistics and diagnostics

## 🛠️ Technologies Used
- **Streamlit**: Web framework for the dashboard
- **Plotly Express**: Interactive visualizations
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

## 🚀 Getting Started

### Prerequisites
```bash
pip install streamlit plotly pandas numpy
```

### Running the Application
```bash
streamlit run app.py
```

## 📁 Project Structure
```
Big_Mart_Sales/
├── .gitignore             
├── README.md                 
├── app.py                      
├── Big_Mart.csv             
├── cleaned_data.csv       
├── Big_Mart_Sales_Notebook.ipynb
├── main.py
└── pyproject.toml              
```

## 📊 Dataset
The dashboard uses Big Mart sales data with the following columns:

**Product Information**
- Item_Identifier, Item_Weight, Item_Fat_Content
- Item_Visibility, Item_Type, Item_MRP

**Outlet Information**
- Outlet_Identifier, Outlet_Establishment_Year
- Outlet_Size, Outlet_Location_Type, Outlet_Type

**Sales Data**
- Item_Outlet_Sales (Target Variable)

## 🎨 Design Features
- **Modern UI**: Clean, professional design with vibrant colors
- **Responsive Layout**: Wide layout optimized for data visualization
- **Interactive Elements**: Hover effects and dynamic filtering
- **Consistent Color Scheme**: Coordinated color palettes across all charts
- **Advanced Analytics**: Multi-dimensional bubble charts and trend analysis

## 📈 Visualization Types
- **Scatter Plots**: Sales vs. MRP relationships
- **Bar Charts**: Category-wise performance analysis
- **Pie Charts**: Distribution and percentage breakdowns
- **Histograms**: Data distribution patterns
- **Line Charts**: Trend analysis over time
- **Box Plots**: Statistical distribution analysis
- **Bubble Charts**: Multi-dimensional performance matrix

## 🎯 Business Value
- **Sales Optimization**: Identify top-performing product categories
- **Inventory Management**: Understand product visibility impact
- **Store Performance**: Compare outlet types and locations
- **Pricing Strategy**: Analyze MRP influence on sales
- **Market Insights**: Fat content preference analysis
- **Predictive Analytics**: Model-based sales forecasting

## 🌟 Key Insights
- **30% Revenue Concentration**: Fruits, Vegetables, and Snack Foods drive major sales
- **Health Trend**: Low Fat products significantly outperform Regular alternatives
- **Price Sensitivity**: Strong correlation between MRP and sales performance
- **Store Hierarchy**: Supermarket Type 3 leads in average sales performance
- **Visibility Factor**: Limited correlation between product visibility and sales

---
*Dashboard created for comprehensive Big Mart sales analysis and business intelligence.*
