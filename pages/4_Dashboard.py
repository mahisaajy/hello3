import streamlit as st
from streamlit_folium import st_folium
import folium
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

st.markdown("# Oceanography ❄️")
st.sidebar.markdown("# Page 3 ❄️")

nc_file = "data/indo_pr_day_EC-Earth3_historical_r1i1p1f1_gr_2013.nc"
data = xr.open_dataset(nc_file)
temperature = data['pr'].isel(time=1).values  # Selecting a single time slice for plotting
lats = data['lat'].values
lons = data['lon'].values
plt.figure(figsize=(10, 6))
contour = plt.contourf(lons, lats, temperature, cmap='RdYlBu')

plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.savefig('contour_plot.png', bbox_inches='tight')
st.pyplot(plt)

m = folium.Map(location=[np.mean(lats), np.mean(lons)], zoom_start=5)
folium.raster_layers.ImageOverlay(
   name='Temperature Contours',
   image='contour_plot.png',
   bounds=[[lats.min(), lons.min()], [lats.max(), lons.max()]],
   opacity=0.5,
   interactive=True,
   cross_origin=False,
   zindex=1,
   # mercator_project=True  # Tambahkan argumen mercator_project=True
).add_to(m)
st.write("Data NetCDF plotted on Leaflet map")
st_folium(m)
