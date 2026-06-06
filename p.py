import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide") # Page ko wide view mein set karein
st.title("High-Performance Graph Generator")

# Caching: File load hone ke baad store ho jayegi, baar-baar process nahi hogi
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

uploaded_file = st.file_uploader("Add CSV File", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    
    col1, col2 = st.columns([1, 3]) # UI ko clean karne ke liye side-by-side layout
    
    with col1:
        st.write("### Settings")
        x_axis = st.selectbox("X-axis:", df.columns)
        y_axis = st.selectbox("Y-axis:", df.columns)
        
    with col2:
        # Plotly ka interactive graph
        fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
        
        # Graph ko aur clean banane ke liye styling
        fig.update_layout(
            plot_bgcolor='white',
            hovermode='x unified'
        )
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        
        st.plotly_chart(fig, use_container_width=True)
