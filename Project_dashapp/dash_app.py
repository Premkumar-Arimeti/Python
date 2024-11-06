import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Data acquisition
df = pd.DataFrame({
    'product_id': [1001, 1002, 1003, 1004],
    'quality_score': [88, 90, 92, 94],
    'test_date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04']
})

# App initialization
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Manufacturing Quality Control Dashboard"),
    dcc.Dropdown(
        id='product-dropdown',
        options=[{'label': str(i), 'value': i} for i in df['product_id'].unique()],
        placeholder="Select Product ID"
    ),
    dcc.Graph(id='quality-chart')
])

# Define callback decorator
@app.callback(
    Output('quality-chart', 'figure'),
    [Input('product-dropdown', 'value')]
)
# Callback function
def update_chart(product_id):
    # Filter data based on selected product_id
    if product_id:
        filtered_data = df[df['product_id'] == product_id]
    else:
        filtered_data = df  # Show all data if no product is selected

    # Create bar chart using Plotly
    fig = px.bar(filtered_data, x='test_date', y='quality_score', title='Quality Score Over Time')
    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
