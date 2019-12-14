import plotly.graph_objects as go
import pandas as pd

data_path = "./data/manias_stannis_series.csv"

df = pd.read_csv(data_path)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.Date, y=df['Manias'], name="Manias expenses",
                         line_color='deepskyblue'))

fig.add_trace(go.Scatter(x=df.Date, y=df['Stannis'], name="Stannis expenses",
                         line_color='dimgray'))

fig.update_layout(title_text='Time Series Manias and Stannis',
                  xaxis_rangeslider_visible=True)
fig.show()