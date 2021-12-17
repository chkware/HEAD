Idea
====

The idea is to create just a REST api testing tools.

Test config:

[**environment**]

1. User creates a config file `project-name.dochk.yml`
    - If no file passed, system try to find a file named `*.dochk.yml`
    - If none found system exits with usage message

2. User can change file name via command line `-f` flag
3. User able to run only selected flows `-r=flow-an,flow-another`
4. Generate settings file from command prompt, with default config
[**configurations**]

Two type of configurations:

1. project configuration to config what you want to achieve.
2. system configuraiton to configure howt `dochk` should behave, and use underlying libs.


[**sample api**]

[google search](https://google.com/search?q=sample+rest+api+server)

[**apidoc format**]
- Open API
- RAML
- Swagger
- API Blueprint
- Postman Collection
- Insomnia Export Format
- HAR?!
