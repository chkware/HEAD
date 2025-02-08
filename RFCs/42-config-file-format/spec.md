# Project config file

Project config files are used to load configuration for the local system.

## Rules 

- This file to be initiated at the beginning of the project.
- This file to be situated at the root of the project

## Problems RFC solves

- Save default system values
  - Path to project (resolved path)
  - Path to log
  - Path to cache
  - ... [tbd]

- Save current projects used modules
  - Module configuraiton parameters

- Ignore section to ignore directory or file
  - For discovery and run cases.

## Spec. structure suggestion

### File name

The file named `.chkconfig`.