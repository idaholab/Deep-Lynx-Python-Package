## Deep Lynx Package Tests

This project uses Pytest.  

The following tests require certain parameters to be set in the test instance of Deep Lynx:  
- `test_upload_file`: The `FILESYSTEM_STORAGE_DIRECTORY` parameter must be set in the Deep Lynx `.env`. Note that this path must end with a directory character (e.g. "/").

To run all tests and view statement coverage, run the following commands:
- `coverage run -m pytest tests/ --cov=deep_lynx --junit-xml=tests/reports/test-results.xml --cov-report html`  
- `python -m http.server`  This will start a web browser to which you can navigate to view all tested files as well as covered and uncovered lines.  
Generally viewable at http://0.0.0.0:8000/htmlcov/  

To run an individual test file, use `pytest tests/test_file_name.py`  
- Option `-rP` can be added to print `print` statements to console during test  
- Option `-k "test_my_test"` may be used to test only the test `test_my_test` in the specified `.py` file  