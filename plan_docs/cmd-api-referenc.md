### Initialize a project

- Generate a .chk file
- Spec file extension (default: `<file_name>.chk`):

```bash
$ chk init
```

### Validate project files

```bash
# if [FILE] or [DIR] not given, then: validate all file of given type
# fx: following command should validate a file given 

$ chk validate [FILE]
$ chk validate file1 file2 ..fileN
```

### Run spec and flow files

```bash
# To run a specification file 
$ chk spec run [SPEC_FILE]

# To run a workflow file 
$ chk spec run [FLOW_FILE]
```