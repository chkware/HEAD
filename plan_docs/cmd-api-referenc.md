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
$ chk validate [FILE]
$ chk validate file1 file2 ..fileN

$ chk validate [DIR]

# example: will validate all .spec.yml of given name
$ chk validate [FILE]
$ chk validate file1 file2 ..fileN

$ chk validate [DIR]

```

### `chk` cli run spec files

```bash
# if [FILE] or [DIR] not given, then: run all file of given type
# running with --all flag should run all the specs in a file
# running without it sould only run default spec
$ chk run [FILE] [DIR] --all
# Eg:
# chk run get_pet_by_id --all


# when run with help command
# chk run get_pet_by_id --help

# Specs:
# get_pet_by_id.get_with_number {pet_id?}
# get_pet_by_id.get_with_string {pet_id?}
# get_pet_by_id.get_without_id {pet_id?}


# Sample commands
# chk run get_pet_by_id.get_with_number
# chk run get_pet_by_id.get_with_number 2

# chk run get_pet_by_id.get_with_string
# chk run get_pet_by_id.get_with_string 'Naseef loves YYYY'

# example: will run all .spec.yml of given name
$ chk run file1 file2 ..fileN
```