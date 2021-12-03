### `chk` cli initialize project


1. Generate a .chk.yml file
2. Name of open api 3 doc (default: `api-docs.yml`):
3. Flow file extension (default: `<file_name>.flow.yml`):
4. Spec file extension (default: `<file_name>.spec.yml`):

```bash
$ chk init

$ chk init -q

# stop generates default template for flow and spec
$ chk init --with-out=flow,spec 
```

### `chk` cli validate project files

```bash
# if [FILE] or [DIR] not given, then: validate all file of given type

# example: will validate all .flow.yml of given name
$ chk flow validate [FILE]
$ chk flow validate file1 file2 ..fileN

$ chk flow validate [DIR]

# example: will validate all .spec.yml of given name
$ chk spec validate [FILE]
$ chk spec validate file1 file2 ..fileN

$ chk spec validate [DIR]

```

### `chk` cli run spec files

```bash
# if [FILE] or [DIR] not given, then: run all file of given type
$ chk spec run [FILE] [DIR]

# example: will run all .spec.yml of given name
$ chk spec run file1 file2 ..fileN

```