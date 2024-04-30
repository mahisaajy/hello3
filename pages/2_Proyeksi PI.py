import streamlit as st
import pandas as pd
import numpy as np

st.title('Proyeksi Perubahan Iklim')

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(df)

data = pd.DataFrame({
    'latitude': [-6.1560067, -6.1754083],
    'longitude': [106.8394085, 106.824584]    
})

st.map(data, zoom=11, size=1000, color='#0044ff')