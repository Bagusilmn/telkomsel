import streamlit as st
import streamlit as st
# import pandas as pd
# import numpy as np
import os as os
from mappopucontro import *

gdf = map_path()
kecamatanList = kecamatan_list()
desalist = desa_list()
productlist = ["semua product", "Indihome", "By.u"]

# Selectbox For Kecamatan and Desa
colKecamatan, colDesa, colProduct, colEmpty = st.columns([0.25, 0.25, 0.25, 0.5])
with colKecamatan:
    selected_kecamatan = st.selectbox("Pilih Kecamatan",["Semua"] + kecamatanList, index=0, key="kecamatan")
with colDesa:
    if selected_kecamatan != "Semua":
        desa_list = sorted(gdf[gdf['WADMKC'] == selected_kecamatan]['NAMOBJ'].unique())
    else:
        desa_list = sorted(gdf['NAMOBJ'].unique())
    selected_desa = st.selectbox("Pilih Desa", ["Semua"] + desalist, index=0, key="desa")
with colProduct:
    selected_Product = st.selectbox("Pilih product", ["Semua"] + productlist, index=0, key="product")


map(st.session_state['kecamatan'], st.session_state['desa'])
index_kecamatan = kecamatanList.index(st.session_state.get("kecamatan"))
