import streamlit as st
import read_person_data
import ekgdata
import matplotlib.pyplot as plt
import numpy as np
import person
from PIL import Image

#%% Zu Beginn

# Lade alle Personen
person_names = read_person_data.get_person_list(read_person_data.load_person_data())

# Anlegen diverser Session States
## Gewählte Versuchsperson
if 'aktuelle_versuchsperson' not in st.session_state:
    st.session_state.aktuelle_versuchsperson = 'None'

## Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'



## TODO: Session State für Pfad zu EKG Daten 

#%% Design des Dashboards

# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sind
st.session_state.aktuelle_versuchsperson = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

# Name der Versuchsperson
st.write("Der Name ist: ", st.session_state.aktuelle_versuchsperson) 

# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen

# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist
# Finde den Pfad zur Bilddatei
if st.session_state.aktuelle_versuchsperson in person_names:
    person_data = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
    st.session_state.picture_path = person_data["picture_path"]
    st.session_state.egk_data_path = person_data["egk_data_path"]
    # st.write("Der Pfad ist: ", st.session_state.picture_path) 

#%% Bild anzeigen

image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.aktuelle_versuchsperson)

#% Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Person
current_egk_data = ekgdata.EKGdata(st.session_state.egk_data_path)
print(current_egk_data)

#%% EKG-Daten als Matplotlib Plot anzeigen
# Nachdem die EKG, Daten geladen wurden
# Erstelle den Plot als Attribut des Objektes
current_egk_data.plot_time_series()
# Zeige den Plot an
st.pyplot(fig=current_egk_data.fig)


# %% Herzrate bestimmen
# Schätze die Herzrate 
current_egk_data.estimate_hr()
# Zeige die Herzrate an
st.write("Herzrate ist: ", int(current_egk_data.heat_rate)) 