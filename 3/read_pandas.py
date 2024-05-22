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
    df = pd.read_csv(path, sep=",")

    # Gibt den geladen Dataframe zurück
    return df

def statistics_power(df):

    # Berechnung der statistischen Kennzahlen
    p_mean = df['PowerOriginal'].mean()
    p_maximum = df["PowerOriginal"].max()

    return p_mean, p_maximum

def statistics_heartrate(df):  

    # Berechnung der statistischen Kennzahlen
    hr_maximum = df["HeartRate"].max()

    return hr_maximum

def plot_power_heartrate(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df, y=["PowerOriginal", "HeartRate"])

    # Hinzufügen von Layout-Elementen
    fig.update_layout(
        xaxis_title="Zeit in s",
        yaxis_title="Power in Watt / Herzfrequenz in bpm")

    
    return fig

def add_HR_Zones(df, max_hr):

    # Definition der Herzfrequenzzonen
    zone_1_min = 0.5*max_hr
    zone_1_max = 0.6*max_hr
    zone_2_max = 0.7*max_hr
    zone_3_max = 0.8*max_hr
    zone_4_max = 0.9*max_hr
    zone_5_max = 1.0*max_hr

    # Hinzufügen der Zonen in df
    df["Zone_1"] = (df["HeartRate"] >= zone_1_min) & (df["HeartRate"] < zone_1_max)
    df["Zone_2"] = (df["HeartRate"] >= zone_1_max) & (df["HeartRate"] < zone_2_max)
    df["Zone_3"] = (df["HeartRate"] >= zone_2_max) & (df["HeartRate"] < zone_3_max)
    df["Zone_4"] = (df["HeartRate"] >= zone_3_max) & (df["HeartRate"] < zone_4_max)
    df["Zone_5"] = (df["HeartRate"] >= zone_4_max) & (df["HeartRate"] < zone_5_max)

    return df

def zone_analysis(df):

    # Berechnung der Dauer in den Zonen
    zone_1 = df["Zone_1"].sum()
    zone_2 = df["Zone_2"].sum()
    zone_3 = df["Zone_3"].sum()
    zone_4 = df["Zone_4"].sum()
    zone_5 = df["Zone_5"].sum()

    return zone_1, zone_2, zone_3, zone_4, zone_5

def mean_power_zone(df):
    
        # Berechnung des durchschnittlichen Power in den Zonen
        mean_power_zone_1 = df[df["Zone_1"]]["PowerOriginal"].mean()
        mean_power_zone_2 = df[df["Zone_2"]]["PowerOriginal"].mean()
        mean_power_zone_3 = df[df["Zone_3"]]["PowerOriginal"].mean()
        mean_power_zone_4 = df[df["Zone_4"]]["PowerOriginal"].mean()
        mean_power_zone_5 = df[df["Zone_5"]]["PowerOriginal"].mean()
        print(df[df["Zone_3"]]["PowerOriginal"])
        return mean_power_zone_1, mean_power_zone_2, mean_power_zone_3, mean_power_zone_4, mean_power_zone_5

if __name__ == "__main__":
    df = read_acivity_csv()
    dfnew = add_HR_Zones(df)
    
