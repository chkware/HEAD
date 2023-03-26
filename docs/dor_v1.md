**Document object representation v1**

- need meta block
  - document unique id
  - document path
  - document mangled name
  - type of document
  - version of the document
  - document unique content hash
- relationship with other documents
  - requires 
- instruction list
  - declare variable
  - set variables
  - get variables
  - request
  - request_from_file
  - assertions

1. The idea of syntax tree
    1. Who can execute this syntax tree? fx: module that contains code to execute this syntax/s

```json
{
    "metadata": {
        "id": "94af621fece419cf9f704c04c4d27af7579c80bf4a9ff4b06c8d83956a50e098",
        "path": "/path/to/file/some-file-name.chk",
        "mangledPath": "system-path-to-file-some-file-name.chk",
        "type": "testcase",
        "version": "0.7.2",
        "contentHash": "c9b6424557416c000b0c75282d6f1f44cd03aaf8ec4c1839789d7edefa71c0b1",
        "contentUpdatedAt": 1678503443
    },
    "requires": [
        {
            "order": 1,
            "documentId": "4e94e534ff65ac2d5c3373d8eae3b8c0b0917d6768c8318431a682c6cc2d3375"
        }
    ],
    "instructionTree": [
        // ...
    ]
}
```

Items under `instructionTree`


