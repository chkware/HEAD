# Project config file

Project config files are used to load configuration for the local system.

## Rules 

- Initiated at the beginning of the project.
- Situated at the root of the project
- File need to be committed to VCS

## Problems RFC solves

- Save default system values
  - Path to project (resolved path)
  - Path to log
  - Path to cache
  - ... [tbd]

- Save current projects used modules
  - Module configuraiton parameters

- Feature flag
  - Experimental module
  - Experimental core features

- Ignore section to ignore directory or file
  - For discovery and run cases.

- Account information [tbd]
- CI/CD pipeliben config [tbd]
- Plugin store path (local)
- Plugin repository path
- Usage telemetry 

## File name

The file named `.chkconfig`.

## Spec. structure

```json
{
  "path": "/Users/0hsn/Works/chkware/cli",
  "path_spec_cache": ".chkware_cache/spec_cache",
  "path_log": ".chkware_cache/log"
}
```