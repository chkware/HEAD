## Variables

The file defines how variables should expected to behave in `chkware`

**Rules**

- There is no pass-by-reference for variables, only pass-by-value
- All variables are public, meaning accessible from outside scope and file
- Use `::import` to include variables from other files to a given file scope
- Use `::invoke` to replace or update variable values from scoped or imported variables
- `{ $var }` is used for variable value replacement

**Usability**

Variables are usable in following specification files

- `http`
- `test-spec`
- `variable`

**Usage**

- define variable like:
    ```yaml
    variables:
        var_1: val
        var-2: val 2
        var3: 'val is three'

        jsonVar: {
            'key_1': val one,
            'key_2': 2,
        }

        long-paragraph: |
            some values can't be changed
            in life.
    ```

    - variable name shouldn't have spaces
    - integers `[0-9]`, underscore `[_]`, dash `[-]` is allowed in variable name, and names can start with those as well.
    - ordering of variable names doesn't matter

- Variable files can be defined as following.
    ```yaml
    # file: Env.chk

    version: 'default:variable:0.7.2'

    varA: GET
    ```

- Variable files can be imported with `::import` key, you can also do named import.
    ```yaml
    # file GetUser.chk

    version: default:test-spec:0.7.2

    variables:
        ::import: [
            'Env'
            'UA': 'Users/UserFullSpec'
        ]
        Method: 'GET'

    request:
        path: "{$Env.server}/user/{$UA.Id}"
        method: $Method

    spec:
        ...
    ```
