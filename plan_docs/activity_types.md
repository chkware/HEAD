activity types:

- executor: system submit form, system follows an URL redirect. There are two type of executor, 
    1. `fetch`
        - call api, *http, https, tcp*
        - download something, *ftp, sftp, http, https*
    2. `exec`
        - command: from commnd line
        - db seed; connect to DB, and NoSQL to run a command

- validator: system validate information received, with given sample   
    - validate with static data
    - validate with regex
    - validate from DB value
    - validate from file text: text, csv, excel

- seeders: system generate data 
    - random data: text, number, URL, etc
    - with given regex or named regex eg: phone, phone_bd
- reports: system generate reports based on exec, test, seed
- mock:
    1. Mock server
- processor
    1. `proc` 
