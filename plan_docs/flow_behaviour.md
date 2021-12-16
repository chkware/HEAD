behaviour of a flow

- can call spec/s
- can call flow/s
> means multiple steps
> multiple step need some boundary on expression


- assert exposed values
- impose / inject values before running specs / flows
- impose / inject values in run context env

### Flow execution type
- sequential
- selective
- iterative
- recursive
- nondeterministic
- concurrent

### Ingredients of flow

```
- {run: '', vars: '', when: '', assert: ''}
- {exec: '', vars: '', when: '', assert: ''}
- {break: '', vars: '', when: ''}
- {continue: '', vars: '', when: ''}
```


### operator used in `when` and `exec`
```
_lt_, _lte_, _gt_, _gte_, _eq_, _neq_,  # comparison
_add_, _sub_, _mul_, _div_, _mod_       # arithmatic
_and_, _or_, _xor_, _not_               # logical
```