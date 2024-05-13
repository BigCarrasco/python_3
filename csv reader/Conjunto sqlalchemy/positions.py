import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('POSITIONS.csv')

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/academy')


df.to_sql('positions', con=engine, if_exists='append', index=False)


print("Los datos han sido guardados en la base de datos MySQL correctamente.")
