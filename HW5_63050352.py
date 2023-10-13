import streamlit as st
import math

st.markdown("<h6 style='text-align: left; color: green;'>VIRASIT KEAWKAE 63050352</h1>", unsafe_allow_html=True)

def calculate_MVAbf(Z, MVA):
    MVAbf = (100/Z)*MVA
    return MVAbf

def calculate_dc(MVAbf, t):
    dc = (2.65 * MVAbf * t) ** 0.5
    return dc

def calculate_F(MVA, Vac, Z):
    F = (((MVA*10**6)/(math.sqrt(3) * Vac))*100/Z)/1000
    return F

def calculate_emb(D, t, F):
    emb = 1038.7 * (D ** -1.4738) * t * (0.0093*(F**2) - 0.34543*F + 5.9675)
    return emb

def calculate_HRC(emb):
    if emb >= 40.00:
        HRC = "CAT 4"
    elif emb >= 25.00:
        HRC = "CAT 3"
    elif emb >= 8.00:
        HRC = "CAT 2"
    elif emb >= 4.00:
        HRC = "CAT 1"
    elif emb >  0 :
        HRC = "CAT 1"
    else:
        HRC = "Not Defined"
    return HRC

st.header('Enter Parameters')

input_col1, input_col2 = st.columns(2)

MVA = input_col1.number_input('MVA value', value=1.0)
t = st.number_input('t value', value=1.0, format="%.4f")
Z = input_col1.number_input('Z value', value=1.0)

D = input_col2.number_input('D value', value=1.0)
Vac = input_col2.number_input('Vac value', value=1.0)

MVAbf = calculate_MVAbf(Z, MVA)

F = calculate_F(MVA, Vac, Z)

dc = calculate_dc(MVAbf, t)
dc_inches = dc * 12  
emb = calculate_emb(D, t, F)

HRC = calculate_HRC(emb)

output_col1, output_col2, output_col3 = st.columns(3)

with output_col1:
    st.markdown(f"**Fault Current (Isc):** `{F:.4f} kA`", unsafe_allow_html=True)

with output_col1:
    st.markdown(f"**Flash Protection Boundary (Dc):** `{dc:.4f} ft ({dc_inches:.4f} inches)`", unsafe_allow_html=True)

with output_col2:
    st.markdown(f"**Incident Energy (EMB):** `{emb:.4f} cal/cm^2`", unsafe_allow_html=True)

with output_col3:
    st.markdown(f"**Hazard Risk Category (HRC):** `{HRC}`", unsafe_allow_html=True)
