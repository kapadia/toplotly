toplotly
========

Pipe data to Plotly for quick visualizations.

Setup
-----

Two environment variables need to be set.

.. code-block:: bash

    export PLOTLY_USERNAME=akapadia
    export PLOTLY_API_KEY=some-api-key


Example
-------

Suppose you have JSON formatted data,

.. code-block:: bash

    $ cat cloud-cover-over-stgo.json
    [
      {
        "sceneid": "LC82320842015133LGN00",
        "acquisitionDate": "2015-05-13T14:26:54Z",
        "cloud_cover": "7.11"
      },
      {
        "sceneid": "LC82320852015133LGN00",
        "acquisitionDate": "2015-05-13T14:27:18Z",
        "cloud_cover": "20.54"
      },
      {
        "sceneid": "LC82320832015133LGN00",
        "acquisitionDate": "2015-05-13T14:26:30Z",
        "cloud_cover": "7.67"
      },
      {
        "sceneid": "LC80010822015131LGN00",
        "acquisitionDate": "2015-05-11T14:38:30Z",
        "cloud_cover": "2.84"
      }
      ...
    ]
    
    $ cat cloud-cover-over-stgo.json | toplotly 'Cloud cover over Santiago'
