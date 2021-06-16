# Deep Lynx Python Package  
Deep Lynx Python Package

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
  
  
## Installation  

`pip install deep-lynx`   

## Contributing
After cloning the repository, please use [Poetry](https://python-poetry.org/) for setup (e.g. `poetry install`, `poetry shell` to activate the virtual environment, etc).  

Tests can be run with an active and reachable instance of Deep Lynx. Create a file named `.env` at the root of the project. Then fill it out with the following parameters:  

```
DEEP_LYNX_URL=  
CONTAINER_NAME=  
DATA_SOURCE_NAME=  
```

See `tests/REAMDE.md` for more information.  

This project uses [yapf](https://github.com/google/yapf) for formatting. Please install it and apply formatting before submitting changes (e.g. `yapf src/deep_lynx tests --in-place --recursive --style={column_limit:120}`)  

### Other Software
Idaho National Laboratory is a cutting edge research facility which is a constantly producing high quality research and software. Feel free to take a look at our other software and scientific offerings at:

[Primary Technology Offerings Page](https://www.inl.gov/inl-initiatives/technology-deployment)

[Supported Open Source Software](https://github.com/idaholab)

[Raw Experiment Open Source Software](https://github.com/IdahoLabResearch)

[Unsupported Open Source Software](https://github.com/IdahoLabCuttingBoard)

### License

Copyright 2021 Battelle Energy Alliance, LLC

Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  https://opensource.org/licenses/MIT  

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Licensing
-----
This software is licensed under the terms you may find in the file named "LICENSE" in this directory.


Developers
-----
By contributing to this software project, you are agreeing to the following terms and conditions for your contributions:

You agree your contributions are submitted under the MIT license. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer.
