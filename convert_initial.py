import pandas as pd

df = pd.read_excel('BD_Inicial.xlsx')

print(df.columns)

translation_dict = {'NúmeroCaso': 'Case_Number',
                    'Ano': 'Year',
                    'Data': 'Date',
                     'Hora_UTC' : 'Hour',
                     'Período' : 'Period',
                     'Estado_Costeiro': 'Coastal_State',
                     'Resumo' : 'Summary',
                     'Navio' : 'Ship_Name',
                     'Tipo_Navio' : 'Ship_Type',
                     'Bandeira' : 'Flag',
                     'Estado do Navio' : 'Ship_State',
                     'Proximidade_Costa(milhas)' : 'Distance_from_Coast',
                     'ÁREA_NAVEGAÇÃO' : 'Navigation_Area',
                     'Classificação_Ataque' : 'Attack_Classification',
                     'N_Criminosos' : 'N_of_Criminals',
                     'Armamento' : 'Weaponry',
                     'Hijack' : 'Hijack',
                     'Sequestro' : 'Kidnapping',
                     'N_Sequestrados' : 'N_Kidnapping',
                     'Rapto' : 'Abduction',
                     'N_Raptados' : 'N_Abducted',
                     'Feridos' : 'Injured',
                     'N_Feridos': 'N_injured',
                     'Mortos' : 'Dead',
                     'N_Mortos': 'N_Dead',
                     'MedidasProteção' : 'Protection_Measures',
                     'Alarme': 'Alarm',
                     'Ajuda_Autoridades' : 'Assistance_from_Authorities',
                     'Equipa_Segurança' : 'Security_Team',
                     'CIDADELA' : 'Citadel',
                     'Manobra_Evasiva' : 'Evading_Maneuvre',
                     'ValoresRoubados_Navio' : 'Stolen_Values',
                     'Carga_Roubada' : 'Cargo_Theft',
                     'OBS':'Observation'}

# Rename the columns using the dictionary
df = df.rename(columns=translation_dict)

df.to_excel('unprocessed_piracy_guinea_gulf.xlsx')
df.to_csv('unprocessed_piracy_guinea_gulf.csv')