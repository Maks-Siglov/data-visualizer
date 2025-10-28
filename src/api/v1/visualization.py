"""Visualization API endpoints."""

from typing import Literal

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from fastapi.responses import HTMLResponse, Response

from src.services.visualization import VisualizationService
from src.system.resources import IoCContainer

router = APIRouter()



@router.get(
    "/visualize/bar-chart",
    response_class=HTMLResponse,
    summary="Create bar chart visualization",
    description="Generate an interactive bar chart from CSV data"
    )
@inject
async def create_bar_chart(
        title: str = Query(
            "Bar Chart",
            description="Chart title"
            ),
        top_n: int | None = Query(
            None,
            gt=0,
            description="Show only top N records"
            ),
        sort_by: Literal["value", "name"] = Query(
            "value",
            description="Sort data by value or name"
            ),
        output_format: Literal["html", "json"] = Query(
            "html",
            description="Output format: html (interactive chart) or json (chart data)"
            ),
        service: VisualizationService = Depends(Provide[IoCContainer.visualization_service])
        ):
    """
    Create a bar chart visualization from CSV data.

    Columns are auto-detected from the data source.

    Parameters:
    - **title**: Chart title
    - **top_n**: Limit to top N records
    - **sort_by**: Sort by 'value' (descending) or 'name' (ascending)
    - **output_format**: 'html' for interactive chart or 'json' for data

    Returns:
    - HTML with interactive Plotly chart (default)
    - JSON with chart configuration (if output_format=json)
    """
    # Create the chart with auto-detected columns
    fig = service.create_bar_chart(
        title=title,
        top_n=top_n,
        sort_by=sort_by
        )

    # Return based on output format
    if output_format == "json":
        return Response(
            content=fig.to_json(),
            media_type="application/json"
        )
    else:
        # Return as interactive HTML
        return fig.to_html(
            include_plotlyjs="cdn",
            config={
                "displayModeBar": True,
                "displaylogo": False,
                "toImageButtonOptions": {
                    "format": "png",
                    "filename": "bar_chart",
                    "height": 600,
                    "width": 1200
                    }
                }
            )
