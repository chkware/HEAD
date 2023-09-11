# Idea of workflow

Following are key achievable for workflow in CHKware:

- Workflow is a definition spec. file that contains list of tasks to complete.
- It can contain tasks consists of other (allowed) CHKware sub-commands. namely: validate, fetch [... for now]
- It can also contain tasks that describes scripts those can be run using `/usr/bin/env [SCRIPT-RUNTIME]`.
- A workflow can contain another workflow as a task

## Issues

- how to determine fail in fetch?
- how to determine fail in validate?
