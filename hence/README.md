workflow:
- title
- workgroup
    task_function()
    - title
    - task
        - pass_context
        - pass_previous_step
        - pass_steps
        - before
        - after
        - step(title, id)
        - step_function() <- usually functions

Something like:

```python
@pass_context
@pass_previous_step
@pass_steps
@work(id, before=..., after=...)
def step_function(steps, previous_step, context):
    ...
```
