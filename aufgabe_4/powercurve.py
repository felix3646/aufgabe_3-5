from functions import read_acivity_csv, plot_powercurve
import streamlit as st

df = read_acivity_csv()
plot_powercurve(df, 1)