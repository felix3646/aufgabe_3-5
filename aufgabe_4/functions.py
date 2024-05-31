# Paket für Bearbeitung von Tabellen
import pandas as pd

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px
import numpy as np

#Allgemeine Anmerkung 
# mit fs soll die Samplingrate angegeben werden, also wie viele Datenpunkte pro Sekunde vorhanden sind.
# In der Funktion create_power_curve wird die Samplingrate auf 1 gesetzt, da die Datenpunkte pro Sekunde gegeben sind.

def read_acivity_csv():
    # Einlesen eines Dataframes
    path = "data/activities/activity.csv"
    df = pd.read_csv(path, sep=",")

    # Gibt den geladen Dataframe zurück
    return df

def find_best_effort(df, t_interval, fs =1):
    # Berechnung des besten Efforts
    windowsize = t_interval * fs
    meanpower = df["PowerOriginal"].rolling(window = windowsize).mean()
    bestpower = meanpower.max()

    return bestpower

# Funktion zur Erstellung der Powercurve für jede Fenstergröße
def create_power_curve(df, fs = 1):
    intervall = np.array(range(len(df))) / fs
    powercurve = []
    
    for i in intervall:
        i = int(i)
        powercurve.append(find_best_effort(df, i, fs))
    

    df_powercurve = pd.DataFrame({"Powercurve": powercurve, "Intervall": intervall/60})
    return df_powercurve


# Funktion zur Erstellung der Powercurve für vorgegebene einzelne Intervalle
def create_power_curve_easy(df, fs = 1):
    intervall = [1, 5, 10, 30, 60, 120, 180, 300, 600, 1200, 1800, 3600, 5400, 7200]
    # Entfernen von Intervallen, die länger sind als die Länge des Dataframes
    if intervall[-1] >= len(df)/fs:
        while intervall[-1] >= len(df)/fs:
            intervall.pop()
       
    else: # Hinzufügen von Intervallen, sollte das letzte Intervall kürzer sein als die Länge des Dataframes
        while intervall[-1] < len(df/ fs):
            intervall.append(intervall[-1] * 2)
        
    powercurve = []     # Liste für die Powercurve
    
    for i in intervall:     # Berechnung der Powercurve für jedes Intervall
        i = int(i)
        powercurve.append(find_best_effort(df, i, fs))
    df_powercurve = pd.DataFrame({"Powercurve": powercurve, "Intervall": intervall}) # Erstellen des Dataframes
    return df_powercurve

#Funktion zum Plotten der Powercurven
def plot_powercurve(df,fs):
    # Einlesen des Dataframes
    df = read_acivity_csv()
    df_powercurve_easy = create_power_curve_easy(df,fs)
    df_powercurve = create_power_curve(df,fs)

    # Funktion, um Intervalle in Minuten:Sekunden-Format zu konvertieren
    def format_zeit(intervall):
        minuten = intervall // 60
        sekunden = intervall % 60
        return f"{minuten}:{sekunden:02d}"

    # Anwenden der Formatierungsfunktion auf die 'Intervall'-Spalte
    df_powercurve_easy['Formatierter Intervall'] = df_powercurve_easy['Intervall'].apply(format_zeit)

    # Erstellen des Diagramms mit kategorischen x-Achsenbeschriftungen
    fig_curve_sprinter = px.line(df_powercurve_easy, x='Formatierter Intervall', y='Powercurve', title='Powercurve')
    fig_curve_sprinter.update_layout(
        title="Powercurve Ansicht für Sprinter",
        xaxis_title="Intervall (Minuten:Sekunden)",
        yaxis_title="Power in Watt"
    )

    # Zweiter Plot mit linearer Skala auf der x-Achse
    # Erstellen des Diagramms für die Powercurve mit linearer Skala auf der x-Achse
    fig_curve_normal = px.line(df_powercurve, x='Intervall', y='Powercurve', title='Lineare Skala auf der X-Achse')
    fig_curve_normal.update_layout(
        title="Powercurve Normalansicht",
        xaxis_title="Intervall in Minuten",
        yaxis_title="Power in Watt"
    )
    return fig_curve_sprinter, fig_curve_normal

if __name__ == "__main__":

    df = read_acivity_csv()
    plot_powercurve(df, 1)

    fig1, fig2 = plot_powercurve(df, 1)
    fig1.show()
    fig2.show()



