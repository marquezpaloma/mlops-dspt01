import pandas as pd
import streamlit as st
from pathlib import Path

from src.model_monitoring import DataDriftMonitor

st.set_page_config(page_title="Monitoreo de Data Drift", layout="wide")
st.title("Monitoreo de Data Drift")

ROOT = Path(__file__).resolve().parent
df_ref = pd.read_csv(ROOT / "data" / "dataset_limpio.csv")
df_curr = pd.read_csv(ROOT / "data" / "dataset_nuevo.csv")

monitor = DataDriftMonitor(df_ref, df_curr)

column = st.selectbox("Seleccionar variable", df_ref.columns)

ks_stat, p_value = monitor.ks_test(column)
psi_value = monitor.psi(column)
js_value = monitor.jensen_shannon(column)

st.subheader("Métricas de Drift")
st.write("KS:", ks_stat)
st.write("p-value:", p_value)
st.write("PSI:", psi_value)
st.write("Jensen-Shannon:", js_value)

# Semáforo (regla simple por PSI)
if psi_value > 0.2:
    st.error("🚨 Drift significativo detectado")
elif psi_value > 0.1:
    st.warning("⚠️ Drift moderado")
else:
    st.success("✅ Sin drift relevante")