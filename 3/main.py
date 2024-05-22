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

    # Eingabe der Herzfrequenz
    st.title("Maximale Herzfrequenz Eingabe")
    max_hr = st.number_input("Geben Sie ihre maximale Herzfrequenz ein", min_value=100, max_value=250, value=220, step=1)
    st.write("Ihre maximale Herzfrequenz ist: ", max_hr)

    # Daten anzeigen
    st.title("Statistische Kennzahlen")

    p_mean, p_maximum = statistics_power(df)
    p_mean_int = int(p_mean)
    st.write("Der Mittelwert der Leistung beträgt: ", p_mean_int, "Watt")
    st.write("Der Maximalwert der Leistung beträgt: ", p_maximum, "Watt")

    