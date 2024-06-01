from functions import read_acivity_csv, plot_powercurve
import streamlit as st

df = read_acivity_csv()
plot_powercurve(df, 1)

#siehe Funktionsaufruf streamlit die main.py im Ordner aufgabe_3
