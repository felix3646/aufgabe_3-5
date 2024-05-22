import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot, read_acivity_csv, statistics_power, statistics_heartrate, plot_power_heartrate, add_HR_Zones


# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")
    st.write("# My Plot")

    df = read_acivity_csv()
    fig2 = plot_power_heartrate(df)

    st.plotly_chart(fig2)