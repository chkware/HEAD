## API test assertion types

This document lists assertions we need to perform in API tests

- Check status code
- Check node value validation
- Check CRUD effect
- Check data type verification on the request body
- Null Value Check in request body
- Verify length of request data
- Verify Header of the API
- Verify authorization token
- Verify valid email verification on the request body
- Verify required fields are being considered to Create/Update any form
- Verify Path Variables and its value
- Veirfy Environment/Global Variables are being set and storing data as expected
- Verify End point is correct for the API URL
- Verify mandatory properties
- Verify response message
- Verify Response Time
- Verify Request Type
- Validate Response Payload
- Verify proper and relevant error message is received for negative testing


## Assertions

- [ ] assertIsMap
- [ ] assertIsList
- [ ] assertIsBool
- [ ] assertIsFloat
- [ ] assertIsInt
- [ ] assertIsNumeric
- [ ] assertIsString
- [ ] assertIsNotNumeric
- [ ] assertNull
- [x] assertEmpty : object
- [x] assertEquals : object
- [x] assertFalse : bool
- [x] assertTrue

- [ ] assertListContains:list
- [ ] assertMapContains: dict
- [ ] assertStrContains: str

- [ ] assertMapHasKey: dict
- [ ] assertMapHasKeys: dict
- [ ] assertMapDonotHasKeys: dict
- [ ] assertMapExactKeys: dict
- [ ] assertMapKeyCount: dict

- [ ] assertListHasIndex: list

- [ ] assertCount: list

- [ ] assertGreaterThan: int, float
- [ ] assertGreaterThanOrEqual: int, float
- [ ] assertLessThan: : int, float
- [ ] assertLessThanOrEqual: : int, float