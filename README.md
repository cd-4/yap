# YAP

YAP is an API testing framework composed entirely of YAML files.

Here is the basic structure

```yaml

variables:
  # Specify URLS and parameters for use here
  backend_url:
    env: BACKEND_URL
    default: http://localhost:8080
  username:
    env: SAMPLE_USERNAME
    default: test-user123

tests:




```
