import typing

import hence


class Step(typing.Protocol):
    steps: List[hence.BaseStep]

    def set_steps(List[hence.BaseStep]) -> bool:
        ...

    def set_step(hence.BaseStep) -> bool:
        ...

    def get_steps() -> List[hence.BaseStep]:
        ...


class Task(typing.Protocol):
    steps: List[hence.BaseStep]

    def set_steps(List[hence.BaseStep]) -> bool:
        ...

    def set_step(hence.BaseStep) -> bool:
        ...

    def get_steps() -> List[hence.BaseStep]:
        ...


class Workflow(typing.Protocol):
    tasks: List[hence.BaseTask]

    def set_tasks() -> bool:
        ...

    def set_task() -> bool:
        ...

    def get_tasks() -> List[hence.BaseTask]:
        ...


class SampleStep(hence.AbstractStep):
    def __init__(self, title: str, *args, **kwargs) -> None:
        super().__init__(self, title, *args, **kwargs)


class SampleTask(hence.AbstractTask):
    def __init__(self, title: str, *args, **kwargs) -> None:
        super().__init__(self, title, *args, **kwargs)


class SampleWorkflow(hence.AbstractWorkflow):
    def __init__(self, title: str, *args, **kwargs) -> None:
        super().__init__(self, title, *args, **kwargs)


stp_1 = SampleStep()
stp_1.set_step()

tsk_1 = SampleTask()
tsk_1.set_step()

sw = SampleWorkflow("Sample workflow")
sw.set_task(tsk_1)


# ----
# from: https://www.online-python.com/
# ----

def sum(a, b):
    return (a + b)
    
class Aine:
    def __call__(self):
        ...
        
aine = Aine()
        
class Bine:
    def some_fn(self):
        ...
        

print("Is callable -> sum: ", callable(sum), type(sum))
print("Is callable -> Bine.some_fn: ", callable(Bine.some_fn), type(Bine.some_fn))
print("Is callable -> Aine: ", callable(Aine), type(Aine))
print("Is callable -> aine: ", callable(aine), type(aine))

# Is callable -> sum:  True <class 'function'>
# Is callable -> Bine.some_fn:  True <class 'function'>
# Is callable -> Aine:  True <class 'type'>
# Is callable -> aine:  True <class '__main__.Aine'>