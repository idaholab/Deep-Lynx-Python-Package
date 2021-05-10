# Deep Lynx Python Package  

Allows applications to interact with the [Deep Lynx](https://github.com/idaholab/Deep-Lynx) data warehouse.  

```python
import deep_lynx_service

dl_service = deep_lynx_service.DeepLynxService('http://127.0.0.1:8090', 'MyContainer', 'MyDatasource')

# create container
dl_service.create_container(
  {
    'name': 'MyContainer',
    'description': 'My test container'
  }
)

# ensure data source exists or create it
dl_service.init()

# import data to deep lynx
dl_service.create_manual_import(
  dl_service.container_id,
  dl_service.data_source_id,
  {'your data here': 'data'}
)
```

**DeepLynxService** includes a few helper methods for container verification, data source verification and creation, setting auth headers, and retrieving the latest import time. The majority of the class methods are API calls to Deep Lynx. Please see the Deep Lynx [API Documentation](https://github.com/idaholab/Deep-Lynx/tree/master/API%20Documentation) for further details.  

# Installation

# Contributing
After cloning the repository, please use [Poetry](https://python-poetry.org/) for setup (e.g. `poetry install`, `poetry shell` to activate the virtual environment, etc).  

Tests can be run with an active and reachable instance of Deep Lynx. Create a file named `.env` at the root of the project. Then fill it out with the following parameters:  

```
DEEP_LYNX_URL=  
CONTAINER_NAME=  
DATA_SOURCE_NAME=  
```

See `tests/REAMDE.md` for more information.  
