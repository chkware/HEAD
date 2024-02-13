workflow:
- title
- tasks
    @task(title="")
    task_function()
    - title
    - setps
        @push_global
        @push_previous_step
        @push_previous_steps
        @before_hook
        @after_hook
        @step(title, id)
        step_function() <- usually functions