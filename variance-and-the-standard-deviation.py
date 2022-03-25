# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections

df2=df[df['grade'] == 'A'][['score', 'grade']]

variance = ((df2['score'] - df2['score'].mean())**2).mean()

deviation = variance**0.5

df3 = pd.DataFrame({'variance': [variance], 'std_deviation' : [deviation]})
