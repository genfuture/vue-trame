r"""
Installation requirements:
    pip install trame trame-vuetify trame-plotly
"""

from flask import Flask, jsonify
from flask_cors import CORS
import plotly.graph_objects as go
import plotly.express as px

app = Flask(__name__)
CORS(app)

# Keep the existing plot functions (contour_plot, bar_plot, scatter)
# ...

def contour_plot():
    """https://plotly.com/python/contour-plots/"""
    return go.Figure(
        data=go.Contour(
            z=[
                [10, 10.625, 12.5, 15.625, 20],
                [5.625, 6.25, 8.125, 11.25, 15.625],
                [2.5, 3.125, 5.0, 8.125, 12.5],
                [0.625, 1.25, 3.125, 6.25, 10.625],
                [0, 0.625, 2.5, 5.625, 10],
            ]
        )
    )


def bar_plot(color="Gold"):
    return go.Figure(data=go.Bar(y=[2, 3, 1], marker_color=color))


def scatter():
    df = px.data.iris()

    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title="Using The add_trace() method With A Plotly Express Figure",
    )

    fig.add_trace(
        go.Scatter(
            x=[2, 4],
            y=[4, 8],
            mode="lines",
            line=go.scatter.Line(color="gray"),
            showlegend=False,
        )
    )

    return fig


PLOTS = {
    "Contour": contour_plot,
    "Bar": bar_plot,
    "Scatter": scatter,
}

@app.route('/plot/<plot_type>')
def get_plot(plot_type):
    if plot_type in PLOTS:
        fig = PLOTS[plot_type]()
        return jsonify(fig.to_json())
    return jsonify({"error": "Invalid plot type"}), 400

if __name__ == "__main__":
    app.run(debug=True)