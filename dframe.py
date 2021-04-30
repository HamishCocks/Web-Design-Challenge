import pandas as pd

df = pd.read_csv("WebVisualisations\cities.csv")
df.set_index("City_ID", inplace = True)

html_tab = df.to_html('citiess.html')