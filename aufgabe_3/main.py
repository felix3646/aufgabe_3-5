import sys
import os
import streamlit as st

# Den Pfad des übergeordneten Verzeichnisses hinzufügen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importieren der Funktionen
from read_pandas import read_my_csv
from read_pandas import make_plot, read_acivity_csv, statistics_power, statistics_heartrate, plot_power_heartrate
from read_pandas import add_HR_Zones, plot_power_zone_analysis, plot_zone_analysis, zone_analysis, mean_power_zone
from aufgabe_4.functions import read_acivity_csv, plot_powercurve
from aufgabe_4.polar_dominic import read_acivity_csv_polar, plot_powercurve_polar

# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2, tap3, tap4  = st.tabs(["EKG-Data", "Power-Data" , "Powerkurve Ergometer", "Powerkurve Laufen"] )

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:

    #plot1 anzeigen
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

    #plot2 anzeigen
    st.title("Zeitdauer in den Herzfrequenzzonen") 
    dfnew = add_HR_Zones(df, max_hr)

    plot_Zeitdauer = plot_zone_analysis(*zone_analysis(dfnew))
    st.plotly_chart(plot_Zeitdauer)

    #plot3 anzeigen
    st.title("Durchschnittliche Leistung in den Herzfrequenzzonen")
    plot_power_zone = plot_power_zone_analysis(*mean_power_zone(dfnew))
    st.plotly_chart(plot_power_zone)

with tap3:
    st.header("Powerkurve Ergometer")
    
    df = read_acivity_csv()
    # Eingabe der Samplingfrequenz
    st.title("Eingabe der Samplingfrequenz")
    fs = st.number_input("Geben Sie die Samplingfrequenz der csv ein", min_value=1, max_value=100, value=1, step=1, key="fs")
    st.write("Die eingegebene Samplingfrequenz ist: ", fs)

    fig_curve_sprinter, fig_curve_normal = plot_powercurve(df,fs)

    st.plotly_chart(fig_curve_sprinter)
    st.plotly_chart(fig_curve_normal)

with tap4:
    st.header("Powerkurve Laufen")
    
    df_polar = read_acivity_csv_polar()
    # Eingabe der Samplingfrequenz
    st.title("Eingabe der Samplingfrequenz")
    fs1 = st.number_input("Geben Sie die Samplingfrequenz der csv ein", min_value=1, max_value=100, value=1, step=1, key="fs1")
    st.write("Die eingegebene Samplingfrequenz ist: ", fs1)

    fig_curve_sprinter, fig_curve_normal = plot_powercurve_polar(df_polar,fs1)

    st.write("Info: Die CSV Daten stammen aus einem 16km Laufwettkampf")
    st.plotly_chart(fig_curve_sprinter)
    st.plotly_chart(fig_curve_normal)




    