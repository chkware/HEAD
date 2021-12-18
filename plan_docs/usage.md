Introduced convensions
======================

**camel_case**

    - file names
    - variable names
    - values

Why
- lowest common denominator(?!) among all oses, including legecy one
- easy to read, noob friendly, not same for camelCase
- on doubleclick selects whole word, not same of pascal-case

> vars

    - var1: type

definition of variables to be used. 
types: scaler(`bool`, `int`, `double`, `string`), composite(`list`, `dict`, `tuple`), abstract(`void`, `any`)

variables are of two types: `scoped` and `global`. see **file** section for `global` variable files. `scoped` variables are defined with _vars_ keyword.

```
# variable documentation (should we!?)
# ----------------------
vars:
  a_var:
    _ref_: variable interpolation
    _expose_: bool
    _val_: null
```

> specs

listed specifications. type `array`. holds all the specificaitons for a given path to test. Following is so far used childrens.

      # name of the spec
      it:
      
      # pass or fail
      expect: pass
      
      # with var1 and var2
      with:
        var1: value1
        var1: :function param1 param2
      
      # test without var1, array
      without:
        - var1