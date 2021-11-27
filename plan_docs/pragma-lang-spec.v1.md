## Initial idea

### Focus

- Need to be very simple, so that non-tech savvy people can use.


### Language spec

- Block support with `()`. 
> ( code block )

- Comment support with `#`.
> \# Set semVer "0.1.0"

- Variables have 2 different scope. 1) Global, 2) Local, 3) Local Temporary

- Function support with `Function ..param`
> Parse "/(.*)@myemail\.com/i" email

- Loop support with `Loop` and `LoopEach`
> (Loop 1 21 )

- Test conditions with `When` and `Unless`
> When param1 param2

- Event listener with `Watch`
> Watch global.variable



### Functions doc

```
def: Arg
ex:  (Arg)
```
```
def: Expose var1
ex:  (Expose pet_name)
```
```
def: Set variableName value
ex:  Set semVer "0.1.0"
```
```
# not here
def: Parse "regex" value
ex:  Parse "/(.*)@myemail\.com/i" email
```
```
def: Loop startPos endPos step
ex:  Loop 1 20 1
(Loop 1 20
    | Dump (Format "%d" loop.index)
    | Dump loop)

loop.index :The current iteration of the loop. (0 indexed)
loop.first :True if first iteration
loop.last  :True if last iteration
loop.step  :Size of step
loop.len   :The number of items in the sequence
```
```
def: LoopEach iteratorVar
ex:  LoopEach tmp.some_parsed_var

loop.index :The current iteration of the loop. (0 indexed)
loop.item  :The current iteration of the loop value
loop.first :True if first iteration
loop.last  :True if last iteration
loop.len   :The number of items in the sequence
```
```
def: Dump variable
ex:  Dump tmp.some_parsed_var
```
```
def: Format "format specifier string" param1, param2, ...paramN
ex:  Format "%s: %d" name id
ex:  Format "%{name}: %{id}"
```
