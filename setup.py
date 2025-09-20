from setuptools import setup

# This setup.py file overrides any pyproject.toml and forces pip usage
setup(
    name="big-mart-sales-dashboard",
    version="1.0.0",
    description="Big Mart Sales Dashboard",
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=2.0.0", 
        "plotly>=5.15.0",
        "numpy>=1.24.0"
    ]
)