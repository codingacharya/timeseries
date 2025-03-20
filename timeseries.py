import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit Page Config
st.set_page_config(page_title="Time Series Analysis", layout="wide")

# Define metallic colors
metallic_colors = {
    "thick_gold": "#B8860B",
    "light_silver": "#C0C0C0",
    "thick_steel": "#708090",
    "light_gold": "#FFD700"
}

# App Title
st.title("📈 Time Series Analysis with Metallic Theme")

# File uploader
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=True, infer_datetime_format=True)
    st.write("### Data Preview:")
    st.dataframe(df.head())
    
    # Select Date Column
    date_col = st.selectbox("Select Date Column", df.columns)
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])
    df = df.sort_values(by=date_col)
    
    # Select Value Column
    value_col = st.selectbox("Select Value Column", df.columns)
    
    # Plot Time Series
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df[date_col], df[value_col], color=metallic_colors['thick_gold'], linewidth=2, label="Trend")
    ax.set_title("Time Series Trend", fontsize=14, color=metallic_colors['thick_steel'])
    ax.set_xlabel("Date", fontsize=12, color=metallic_colors['light_silver'])
    ax.set_ylabel("Value", fontsize=12, color=metallic_colors['light_silver'])
    ax.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)
    
    # Moving Average
    window = st.slider("Select Moving Average Window", min_value=3, max_value=30, value=7)
    df['Moving_Avg'] = df[value_col].rolling(window=window).mean()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df[date_col], df[value_col], color=metallic_colors['thick_gold'], linewidth=1, alpha=0.6, label="Original")
    ax.plot(df[date_col], df['Moving_Avg'], color=metallic_colors['light_gold'], linewidth=2, label=f"{window}-day MA")
    ax.set_title("Moving Average", fontsize=14, color=metallic_colors['thick_steel'])
    ax.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)
    
    # Display Basic Statistics
    st.write("### Data Statistics")
    st.write(df[value_col].describe())
else:
    st.write("Please upload a CSV file to begin analysis.")