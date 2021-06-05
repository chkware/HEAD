### Sample flow

###### ONLY API testing

1. URI can be `query_string` or _REST_ based
2. response can be JSON, XML
- user register email
  - submit: get success resonse
    - get specific header
  - check inbo
- user verify email
  - follow link
    - can have many links in email
- user register information (2nd part)
  - submit: can get `access_token`
- user login
  - submit: email/username/password/code
  - can get `access_token` & `refresh_token`
  - can get http header 
    - session based stateful api
  - might need to preserve some data to be used in request
    - from `HEADER` or `RESPONSE`
- user can update company information
  - submit: gets success response
- user can update company details information
  - submit: gets success response