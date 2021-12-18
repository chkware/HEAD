## Spec

This document gives information on `Spec` files.

### Example
- This following example requesting and just validating if the response code is 200 `https://reqres.in/users/1` api. So, that we can use it as REST client.

    ```yaml
    version: Rest-Runner/Basic:Spec:0.6

    request:
        url: https://reqres.in/users/1
        method: GET
    ```

- More complex example requesting and validating `https://reqres.in/users` api. Here we can use it as REST client, and a test specification runner tool. [See here](#about-v.chk-files) about `.v.chk` files here

    ```yaml
    # env.v.chk
    server: https://reqres.in/api

    # users.chk

    version: Rest-Runner/Basic:Spec:0.6
    describe: users $page

    vars:
        $page: ~

    request:
        method: GET
        url: 
            path: "{$env.server}/users"
            query_vars:
            page: $page

    spec:
        request_with:
            $page: 1
        asserts:
            - {type: AssertEquals, actual: .code, expected: 200}
    ```

[More sample](#more-spec-samples) can be found here

### Parameters details

- `version` 

    Version of the document, to be used by driver parsers. usual format `driver:operation:version`. [See here](#driver-version-doc)

- `describe` 

    keyword is used to describe how a specification should be called. 
  - Optional, if `describe` is not found on a spec, then file name is called as default `describe` value. 
  - If `describe` value given, then it should match file name.
  - we can also pass variables in describe. [See here](#variable-in-describe)

- `vars`

    This section should be used to define and set default values to variable to be used thorough out a `Spec` file. [See here](#variables) about variables.

- `request`

    Request params to be used for URL fetching. [see here](#request) about request
