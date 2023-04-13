import pandas as pd

df = pd.read_excel('Base_Dados_Final.xlsx', sheet_name='BD')

list(df)

# Define a dictionary with the old column names as keys and new column names as values
translation_dict = {'Período': 'Period', 
                    'Estado_Costeiro': 'Coastal_State', 
                    'Tipo_Navio': 'Ship_Type', 
                    'Bandeira': 'Flag', 
                    'Estado do Navio': 'Ship_State', 
                    'Proximidade_Costa(milhas)': 'Distance_from_Coast', 
                    'ÁREA_NAVEGAÇÃO': 'Navigation_Area', 
                    'Classificação_Ataque': 'Attack_Classification', 
                    'Numero_Criminosos': 'N_of_Criminals', 
                    'N_Criminosos': 'N_of_Criminals_cat', 
                    'Armamento': 'Weaponry', 
                    'Hijack': 'Hijack', 
                    'Sequestro': 'Kidnapping', 
                    'Rapto': 'Abduction', 
                    'Feridos': 'Injured', 
                    'Mortos': 'Dead', 
                    'Nível_Proteção': 'Protection_Level', 
                    'Resumo': 'Summary', 
                    'Data_hora': 'Date_Time', 
                    'vento_tam': 'Wind_Speed', 
                    'vento_nova': 'Wind_Speed_cat', 
                    'vento': 'Wind_Speed_cat_2', 
                    'onda_nova': 'Wave_Size_cat', 
                    'onda': 'Wave_Size_cat_2', 
                    'onda_tam': 'Wave_Size', 
                    'chuva': 'Rain_cat', 
                    'chuva (mm/dia)': 'Rain', 
                    'DATA': 'Date', 
                    'Ano': 'Year', 
                    'Mês': 'Month', 
                    'Estação_Africa': 'African_Season', 
                    'Estação': 'Season', 
                    'Zona_Costeira': 'Coastal_Zone', 
                    'Meteorologia': 'Meteorology', 
                    'Meteorologia_nova': 'New_Meteorology', 
                    'Nível_Ataque': 'Attack_Level', 
                    'Risco_Bandeira': 'Flag_Risk', 
                    'Sucesso_Ataque': 'Attack_Success', 
                    'lat_d': 'Lat_D', 
                    'lon_d': 'Lon_D', 
                    'Ajuda_Autoridades': 'Assistance_from_Authorities', 
                    'Perigosidade': 'Dangerousness'}

# Rename the columns using the dictionary
df = df.rename(columns=translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Noturno': 'Night', 
                    'Diurno': 'Day'}

# Use the replace method to translate the values in the Period column
df['Period'] = df['Period'].replace(translation_dict)



# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Nigéria': 'Nigeria', 
                    'Guiné': 'Guinea', 
                    'Camarões': 'Cameroon', 
                    'Benim': 'Benin', 
                    'Gana': 'Ghana',
                    'República Dem. Congo': 'Democratic Republic of the Congo', 
                    'Togo': 'Togo', 
                    'Serra Leoa': 'Sierra Leone', 
                    'Congo': 'Congo', 
                    'Angola': 'Angola',
                    'Costa do Marfim': 'Ivory Coast', 
                    'Gabão': 'Gabon', 
                    'S.Tomé e Príncipe': 'Sao Tome and Principe', 
                    'Libéria': 'Liberia',
                    'Guiné Equatorial': 'Equatorial Guinea', 
                    'Guiné-Equatorial': 'Equatorial Guinea'}

# Use the replace method to translate the values in the Coastal_State column
df['Coastal_State'] = df['Coastal_State'].replace(translation_dict)


# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Outros': 'Other'}

# Use the replace method to translate the values in the Ship_Type column
df['Ship_Type'] = df['Ship_Type'].replace(translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Outros': 'Other', 
                    'IlhasMarshall': 'Marshall Islands', 
                    'Nigéria': 'Nigeria', 
                    'Malta': 'Malta', 
                    'China': 'China', 
                    'Libéria': 'Liberia',
                    'Panamá': 'Panama', 
                    'Singapura': 'Singapore'}

# Use the replace method to translate the values in the Flag column
df['Flag'] = df['Flag'].replace(translation_dict)


# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Navegar': 'Sailing', 
                    'Fundeado': 'Anchored', 
                    'Atracado': 'Docked'}

# Use the replace method to translate the values in the Ship_State column
df['Ship_State'] = df['Ship_State'].replace(translation_dict)


# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Águas Internacionais': 'International Waters', 
                    'Mar Territorial': 'Territorial Waters', 
                    'Área Portuária': 'Port Area'}

# Use the replace method to translate the values in the Navigation_Area column
df['Navigation_Area'] = df['Navigation_Area'].replace(translation_dict)


# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'NCONSEGUIDO': 'Unsuccessful', 
                    'ROUBO': 'Theft', 
                    'SEQUESTRO': 'Kidnapping', 
                    'HIJACK': 'Hijacking', 
                    'RAPTO': 'Abduction'}

# Use the replace method to translate the values in the Attack_Classification column
df['Attack_Classification'] = df['Attack_Classification'].replace(translation_dict)


# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Médio': 'Medium', 
                    'Baixo': 'Low', 
                    'Alto': 'High'}

# Use the replace method to translate the values in the Protection_Level column
df['Protection_Level'] = df['Protection_Level'].replace(translation_dict)

# Convert the Date_Time column to a pandas Datetime data type
df['Date_Time'] = pd.to_datetime(df['Date_Time'])

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Fraco': 'Gentle_breeze', 
                    'Moderado': 'Moderate_breeze', 
                    'Aragem': 'Light_breeze', 
                    'Bafagem': 'Light_air', 
                    'Fresco': 'Fresh_breeze'}

# Use the replace method to translate the values in the Wind_Speed_cat column
df['Wind_Speed_cat'] = df['Wind_Speed_cat'].replace(translation_dict)

df['Wind_Speed_cat_2'] = df['Wind_Speed_cat_2'].replace(translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Pequena Vaga': 'Slight', 
                    'Cavado': 'Moderate', 
                    'Encrespado': 'Smooth'}

# Use the replace method to translate the values in the Wave_Size_cat column
df['Wave_Size_cat'] = df['Wave_Size_cat'].replace(translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Crescente': 'Increasing', 
                    'Mediana': 'Moderate', 
                    'Elevada': 'High'}

# Use the replace method to translate the values in the Wave_Size_cat_2 column
df['Wave_Size_cat_2'] = df['Wave_Size_cat_2'].replace(translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Frio e Húmido': 'Cold and Humid', 
                    'Seco e Quente': 'Dry and Hot'}

# Use the replace method to translate the values in the Africa_Season column
df['African_Season'] = df['African_Season'].replace(translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Primavera': 'Spring', 
                    'Verão': 'Summer', 
                    'Outono': 'Fall/Autumn', 
                    'Inverno': 'Winter'}

# Use the replace method to translate the values in the Season column
df['Season'] = df['Season'].replace(translation_dict)

# Define a dictionary with the numerical codes as keys and English zone names as values
translation_dict = {'Zona 1': 'Zone 1',
                    'Zona 2': 'Zone 2',
                    'Zona 3': 'Zone 3',
                    'Zona 4': 'Zone 4'}

# Use the replace method to translate the values in the Coastal_Zone column
df['Coastal_Zone'] = df['Coastal_Zone'].replace(translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Baixo': 'Low', 
                    'Médio': 'Medium', 
                    'Alto': 'High'}

# Use the replace method to translate the values in the Flag_Risk column
df['Flag_Risk'] = df['Flag_Risk'].replace(translation_dict)

# Define a dictionary with the Portuguese values as keys and English values as values
translation_dict = {'Facas':'Knives', 
                    'Arma de Fogo': 'Firearms',
                    'Desconhecido': 'Unknown'}

# Use the replace method to translate the values in the Flag_Risk column
df['Weaponry'] = df['Weaponry'].replace(translation_dict)

# Drop some variables that are not needed
df.drop(columns=['Wind_Speed_cat_2','Wave_Size_cat_2','New_Meteorology'], inplace=True)


data_final = df[['Period','Date_Time','Date','Year',
                 'Month','Season','African_Season',
                 'Lat_D','Lon_D','Coastal_State',
                 'Coastal_Zone','Distance_from_Coast',
                 'Navigation_Area','Wind_Speed',
                 'Wind_Speed_cat','Wave_Size',
                 'Wave_Size_cat','Rain','Rain_cat',
                 'Meteorology','Ship_Type','Flag',
                 'Ship_State','Flag_Risk','Protection_Level',
                 'N_of_Criminals','N_of_Criminals_cat',
                 'Weaponry','Attack_Classification',
                 'Hijack','Kidnapping','Abduction',
                 'Attack_Level','Dangerousness','Summary',
                 'Injured','Dead','Attack_Success',
                 'Assistance_from_Authorities']]




data_final.to_excel('piracy_guinea_gulf.xlsx')
data_final.to_csv('piracy_guinea_gulf.csv')
data_final.to_pickle('piracy_guinea_gulf.pickle')

''''''''''''''''''''''''''''''''''''''''''''
import folium
from folium.plugins import MarkerCluster
from folium.vector_layers import Rectangle

# Define a function to save the map view as an image
def save_map_view(map):
    map.save('map_view.png')
    
# Get the center latitude and longitude values of the dataframe
center_lat = (df.Lat_D.max() + df.Lat_D.min()) / 2
center_lon = (df.Lon_D.max() + df.Lon_D.min()) / 2

# Calculate the dimensions of the rectangle based on the minimum and maximum latitude and longitude values in the dataframe
width = df.Lon_D.max() - df.Lon_D.min()
height = df.Lat_D.max() - df.Lat_D.min()

# Create a map object centered on the center latitude and longitude values, with an appropriate zoom level
m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

# Create a marker cluster object to group markers together for better performance
marker_cluster = MarkerCluster().add_to(m)

# Loop over each row in the dataframe and add a marker to the map for each location
for index, row in df.iterrows():
    folium.Marker(location=[row['Lat_D'], row['Lon_D']],
                  popup=row[['Date_Time','Attack_Classification','Weaponry']]).add_to(marker_cluster)

# Create a rectangle object with the dimensions and location calculated earlier
rectangle = Rectangle(bounds=[[df.Lat_D.min(), df.Lon_D.min()], [df.Lat_D.max(), df.Lon_D.max()]], 
                      color='red', fill=False).add_to(m)

# Add a custom control to the map to allow the user to save the map view as an image
folium.plugins.Fullscreen().add_to(m)

# Display the map
m.save('piracy.html')



for column in df.columns:
    print(f"Column: {column}")
    print(df[column].value_counts())


for column in df.columns:
    print(f"Column: {column}")
    print(df[column].describe())

