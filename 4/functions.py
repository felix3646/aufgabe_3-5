# Paket für Bearbeitung von Tabellen
import pandas as pd

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px
import numpy as np


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

# Inervalle 
def create_power_curce(df, fs = 1):
    intervall = np.array(range(len(df))) / fs
    powercurve = []
    
    for i in intervall:
        i = int(i)
        powercurve.append(find_best_effort(df, i, fs))
    

    df_powercurve = pd.DataFrame({"Powercurve": powercurve, "Intervall": intervall/60})
    return df_powercurve

if __name__ == "__main__":
    df = read_acivity_csv()
    #print(find_best_effort(df, 30))
    #print(df.head())
    print(create_power_curce(df, 2))


    #plotten
    time_intervals = [1, 5, 10, 30, 60, 300, 600, 1800, 3600]
    fig = px.line(create_power_curce(df, 1), x= "Intervall", y="Powercurve", log_x=True, title='Logarithmische Skala auf der X-Achse')
    layout = fig.update_layout(title="Powercurve", xaxis_title="Intervall in Minuten", yaxis_title="Power in Watt")
   

    fig.show()