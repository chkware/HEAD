activity types:

- executor: system submit form, system follows an URL redirect. There are two type of executor, 
    1. `fetch`
        3. call api, *http, https, tcp*
        4. download something, *ftp, sftp, http, https*
    2. `exec`
        1. command: from commnd line
        2. db seed; connect to DB, and NoSQL to run a command

- validator: system validate information received, with given sample   
    1. validate with static data
    2. validate with regex
    3. validate from DB value
    4. validate from file text: text, csv, excel

- seeders: system generate data 
    1. random data: text, number, URL, etc
    2. with given regex or named regex eg: phone, phone_bd
- reports: system generate reports based on exec, test, seed
- mock:
    1. Mock server
