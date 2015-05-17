toplotly
========

Pipe data to Plotly for quick visualizations.


.. code-block:: bash

    cat chile.geojson | usgs search --node EE LANDSAT_8 | jq -r ".[].entityId" | usgs metadata --node EE LANDSAT_8 --extended | jq '.[] | {sceneid: .entityId, acquisitionDate: .acquisitionDate, cloud_cover: .extended["Scene Cloud Cover"] }' | toplotly 'Cloud cover over Chile'