Node tags can be used like following

```yaml
variables:
    # --- with . and \s ---
    # I admit this is strange, not YMLish, but clean

    child2 .some=int: <% value | lower %>
    parent2 .some='str' .some2 .some3=(1,2,3) .some4=(a:'1',b:'2',c:'3') .some5=false: value

    # --- with [] and | ---
    # not this because it looks bad for multiple tags

    parent2[some=str|some2|some3=1,2,3]: value
    body[xml]: |
       <xml>
         <a int=true>Some</a>
       </xml>

    # --- with [] and & ---
    # not this because it looks bad for multiple tags, not readable

    parent2[some=str&some2&some3=1,2,3]: value    

    # behavior of body, type of body in fetch
    # more example of dot tags

    body .enc=xml: |
       <xml>
         <a int=true>Some</a>
       </xml>

    body .enc=json: {
      a: "val1",
      b: 2
    }

    body:
      a: "val1"
      b: 2
```
