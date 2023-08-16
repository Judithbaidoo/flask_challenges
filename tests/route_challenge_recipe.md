# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Request
GET /names?add=Eddie

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

#GET /names add = Eddie
#  Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

## 3. Test-drive the Route

"""
#GET /names 
# add = Eddie
#  Expected response (200 OK):
Julia, Alice, Karim, Eddie
"""
def test_add_name(web_client):
    response = web_client.get('/names', data ={'name'= 'Eddie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'


