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

# example: will validate all .spec.yml of given name
$ chk spec validate [FILE]
$ chk spec validate file1 file2 ..fileN

$ chk spec validate [DIR]

```

### Run spec and flow files

```bash
# if [FILE] or [DIR] not given, then: run all file of given type
$ chk spec run [FILE] [DIR] --all

# chk run get_pet_by_id --all
# chk spec run get_pet_by_id --help

# Specs:

# get_pet_by_id.get_with_number {pet_id?}
# get_pet_by_id.get_with_string {pet_id?}
# get_pet_by_id.get_without_id {pet_id?}

# chk spec run get_pet_by_id.get_with_number
# chk spec run get_pet_by_id.get_with_number 2

# chk spec run get_pet_by_id.get_with_string
# chk spec run get_pet_by_id.get_with_string 'Naseef loves YYYY'

# example: will run all .spec.yml of given name
$ chk spec run file1 file2 ..fileN

```