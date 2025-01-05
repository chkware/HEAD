```yaml
---
version: default:http:0.7.2

request:
	url: "https://dummyjson.com/users/add"
	method: POST
	headers:
		Accept-Encoding: gzip, deflate
		Content-Type: application/json
	body[form]:
		firstName: "Some"
		lastName: "O' Name"
		age: 51

expose:
	- <% _response %>
```

#### DOCUMENT ACTIVITY

- check document version
	- check version string
	- version wise file format
	- version wise data format for nodes
- prepare data (.. to be used)
	- setup environment variables
	- setup document variables
	- setup passed variables
	- TBD
- process main document
	- replace variables
	- process document
	- update setup data (.. if necessary)
- expose data
	- expose data for console output
	- expose data for module export
	- expose data for session usage (.. need DB support)
