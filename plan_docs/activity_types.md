activity types:

- executor: system submit form, system follows an URL redirect.
    1. `exec`
        - call api with `curl`, *http, https, tcp*
        - download something with `wget`, `curl`, *ftp, sftp, http, https*
        - command: from commnd line
        - db seed; connect to DB, and NoSQL to run a command

- validator: system validate information received, with given sample
    - validate with static data
        - in-place data
        - parameterized data
    - validate with regex
    - validate from DB value
    - validate from file text: text, csv, excel

- seeders: system generate data 
    - random data: text, number, URL, etc
    - with given regex or named regex eg: phone, phone_bd
- reports: system generate reports based on exec, test, seed
- mock:
    1. Mock server
- processor: for before and after hook, can be used in combination with other activity type.
    - `proc`
- storeage: store response
    - `save` 
        - save to disk
        - save to db
        - call url to POST/PUT data