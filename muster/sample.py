import typing

import muster


class Step(typing.Protocol):
    steps: List[muster.BaseStep]

    def set_steps(List[muster.BaseStep]) -> bool:
        ...

    def set_step(muster.BaseStep) -> bool:
        ...

    def get_steps() -> List[muster.BaseStep]:
        ...


class Task(typing.Protocol):
    steps: List[muster.BaseStep]

    def set_steps(List[muster.BaseStep]) -> bool:
        ...

    def set_step(muster.BaseStep) -> bool:
        ...

    def get_steps() -> List[muster.BaseStep]:
        ...


class Workflow(typing.Protocol):
    tasks: List[muster.BaseTask]

    def set_tasks() -> bool:
        ...

    def set_task() -> bool:
        ...

    def get_tasks() -> List[muster.BaseTask]:
        ...


class SampleStep(muster.AbstractStep):
    def __init__(self, title: str, *args, **kwargs) -> None:
        super().__init__(self, title, *args, **kwargs)


class SampleTask(muster.AbstractTask):
    def __init__(self, title: str, *args, **kwargs) -> None:
        super().__init__(self, title, *args, **kwargs)


class SampleWorkflow(muster.AbstractWorkflow):
    def __init__(self, title: str, *args, **kwargs) -> None:
        super().__init__(self, title, *args, **kwargs)


stp_1 = SampleStep()
stp_1.set_step()

tsk_1 = SampleTask()
tsk_1.set_step()

sw = SampleWorkflow("Sample workflow")
sw.set_task(tsk_1)
