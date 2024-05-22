# Paket für Bearbeitung von Tabellen
import pandas as pd

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df



def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig



#df = read_my_csv()
#fig = make_plot(df)

#fig.show()

def read_acivity_csv():

    # Einlesen eines Dataframes
    path = "data/activities/activity.csv"
    df = pd.read_csv(path, sep=",", header=None)

    # Gibt den geladen Dataframe zurück
    return df

def statistics_power(df):
    # Berechnung der statistischen Kennzahlen
    p_mean = df['PowerOriginal'].mean()
    p_maximum = df["PowerOriginal"].max()

    return p_mean, p_maximum


def make_activity_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig


if __name__ == "__main__":
    df = read_acivity_csv()
    print(df.head())

    #meane, maximume = statistics_power(df)
    #print(meane)
    #print(maximume)
