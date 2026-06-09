import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("High-Performance Multi-CSV Graph Generator")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Multiple files upload karne ke liye accept_multiple_files=True add kiya
uploaded_files = st.file_uploader("Add CSV Files", type=["csv"], accept_multiple_files=True)

if uploaded_files:
    # Files ke naam ki list banayi taaki user select kar sake
    file_names = {file.name: file for file in uploaded_files}
    selected_file_name = st.selectbox("Select file to visualize:", list(file_names.keys()))
    
    # Selected file load karein
    df = load_data(file_names[selected_file_name])
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.write("### Settings")
        x_axis = st.selectbox("X-axis:", df.columns)
        y_axis = st.selectbox("Y-axis:", df.columns)
        
    with col2:
        # Plotly graph
        fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis} ({selected_file_name})")
        
        fig.update_layout(
            plot_bgcolor='white',
            hovermode='x unified'
        )
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        st.plotly_chart(fig, use_container_width=True)
        
    # Optional: Data preview dekhne ke liye
    if st.checkbox("Show raw data"):
        st.write(df.head())
