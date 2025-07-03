import random
from llama_index.core.workflow import Event, StartEvent, StopEvent,step, Workflow
import asyncio

class StudentEvent(Event):
    sname: str
    reg: int

class StudentFlow(Workflow):

    @step
    async def generate_student(self, ev: StartEvent) -> StudentEvent:
        regnum = random.randint(1, 10)
        names = ("Alice", "Bob", "Charlie", "Diana", "Eve")
        sname = random.choice(names)
        return StudentEvent(sname=sname, reg=regnum)

    @step
    async def show_student(self, ev: StudentEvent) -> StopEvent:
        print(f"Name: {ev.sname}")
        print(f"Reg no: {ev.reg}")
        return StopEvent(result={"name": ev.sname, "reg": ev.reg})

async def main():
    flow = StudentFlow(timeout=10, verbose=True)
    result = await flow.run()
    print("Final result:", result)

if __name__ == '__main__':
    asyncio.run(main())
