import plotly.graph_objects as go
import numpy as np
import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6 import QtCore, QtWidgets, QtGui

# # Create a 3D scatter plot
# fig = go.Figure(data=[go.Scatter3d(x=[0,1], y=[0,1], z=[0,1], mode='markers', marker=dict(size=8, color=[0,1], colorscale='Viridis'))])
# # Add title and labels
# fig.update_layout(title='3D Scatter Plot', scene=dict(xaxis_title='X-axis', yaxis_title='Y-axis', zaxis_title='Z-axis'))
# # Show the plot
# fig.show()