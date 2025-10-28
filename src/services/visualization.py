
import plotly.express as px
import plotly.graph_objects as go

from src.data_source.base import DataSource


class VisualizationService:
    """Service for creating data visualizations."""

    def __init__(self, data_source: DataSource):
        """Initialize visualization service with a data source.

        Args:
            data_source: Data source implementing IDataSource interface
        """
        self.data_source = data_source

    def create_bar_chart(
            self,
            title: str = "Bar Chart",
            top_n: int | None = None,
            sort_by: str = 'value'
            ) -> go.Figure:
        """Create an interactive bar chart and return as HTML.

        Args:
            title: Chart title
            top_n: If specified, show only top N records
            sort_by: How to sort data ('value' or 'name')

        Returns:
            str: HTML string containing the interactive chart
        """
        # Load data
        df = self.data_source.load_data()

        # Auto-detect columns if not specified
        columns = df.columns.tolist()
        if len(columns) < 2:
            raise ValueError("DataFrame must have at least 2 columns")

        # Try to find a text column and a numeric column
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        text_cols = df.select_dtypes(include=['object']).columns.tolist()

        x_column = text_cols[0] if text_cols else columns[0]
        y_column = numeric_cols[0] if numeric_cols else columns[-1]

        # Prepare data for visualization
        chart_df = df[[x_column, y_column]].copy()
        chart_df.columns = ['label', 'value']

        # Sort data
        if sort_by == 'value':
            chart_df = chart_df.sort_values('value', ascending=False)
        else:
            chart_df = chart_df.sort_values('label')

        # Limit to top N if specified
        if top_n:
            chart_df = chart_df.head(top_n)

        # Create bar chart
        fig = px.bar(
            chart_df,
            x='label',
            y='value',
            title=title,
            labels={'label': x_column, 'value': y_column},
            color='value',
            color_continuous_scale='viridis'
            )

        # Customize layout
        fig.update_layout(
            xaxis_tickangle=-45,
            height=600,
            showlegend=False,
            hovermode='x unified',
            template='plotly_white'
            )

        return fig
