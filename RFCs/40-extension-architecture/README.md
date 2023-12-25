# Extension-based Architecture

An extension based architecture can be introduced to facilitate quick and decentralized feature development. [**_Pluggy_**](https://pluggy.readthedocs.io/en/stable/) extension framework could be used.

## Expectations

- Anybody should be able to create a plugin with less hessel

- Perferablly language platform independent way

- Host/core should be able to access Plugin/client state anytime

- Plugin/client system should be able to 
    - access necessary global state data

    - update necessary global state data

    - NOT be able to mess global state state data

- Plugin/client can also host plugin machanism based on Host/core to swap their feature

- System should have a unified
    - logging / debugging system
    - data bus to 
        - transfer data between other Plugin/client
        - request feature or get response

## Architecture [DRAFT]

### Common steps [fetch]

- load and process console argument
- make execution context
- make file context

### Core requirements
    
- console.parser.parse_variables()
- core.engine.build_file_context()
- core.engine.build_exec_context()
- core.engine.build_context()
- core.engine.set_context_to_env()
- core.engine.main()
- 