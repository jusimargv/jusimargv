import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from pycaret.regression import *
import plotly.graph_objects as go

# Load data from Yahoo Finance
data = yf.download('PETR4.SA', start='2020-01-01', end='2024-06-28')

# Create a dataframe with the closing prices
df = pd.DataFrame(data['Close'])

# Create a new column with the direction of the movement (up or down)
df['Movement'] = df['Close'].pct_change().apply(lambda x: 1 if x > 0 else 0)

# Split the data into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Create a PyCaret regression model
exp = setup(train_df, target='Movement')

# Compare different models
best_model = compare_models()

# Tune the best model
tuned_model = tune_model(best_model)

# Make predictions on the test set
predictions = predict_model(tuned_model, data=test_df)

# Plot the results using Plotly
fig = go.Figure(data=[go.Scatter(x=test_df.index, y=test_df['Close'], name='Actual'),
                     go.Scatter(x=test_df.index, y=predictions, name='Predicted')])
fig.update_layout(title='Petrobras (PETR4) Stock Price Movement Prediction',
                  xaxis_title='Date', yaxis_title='Price')
fig.show()