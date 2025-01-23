#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#%%
df= pd.read_csv('main\dataset\global_terrorism.csv',encoding='ISO-8859-1')
df.head(5)
#%%
df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','provstate':'state',
                     'region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed',
                     'nwound': 'Wounded','gname':'Group','targtype1_txt':'Target_type',
                     'weaptype1_txt':'Weapon_type'
                    },inplace=True)
#%%
df.isnull().sum()
#%%
#%%
df.info()
#%%
df = df[['eventid','Year','Month','Day','latitude','longitude','AttackType','Killed','Wounded','Group','Target_type','Weapon_type','success']]
#%%
df.isnull().sum()
#%%
for col in df.select_dtypes(include=['object']).columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df.info()
#%%
# Calcular a matriz de correlação
correlacao = df.corr()

# Criar o mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Adicionar título
plt.title('Mapa de Correlação')
plt.show()
#%%
















# %%
