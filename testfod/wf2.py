import random
import asyncio
from llama_index.core.workflow import Event, StartEvent, StopEvent,step, Workflow, Context
from sqlalchemy import create_engine,text

class friends(Event):
    fid:int

class connEvent(Event):
    conn: any

class friendsFlow(Workflow):
    
    @step
    async def generate_number(self, ctx:Context, ev: StartEvent) -> friends:
        regno:int = random.randint(1,5)
        ctx.data["regno"] = regno
        return friends(fid=regno)
        
    @step
    async def generate_conn(self, ctx:Context, ev:StartEvent) -> connEvent:
        engine = await create_engine("mssql+pyodbc://@DESKTOP-M8HIIN2\\SQLEXPRESS02/sqlalc?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes",echo=True)
        conn=engine.connect().execution_options(isolation_level="AUTOCOMMIT")
        ctx.data["conn"] = conn
        print('Connection success!')
        return conn
    
    @step
    async def get_details(self, ctx: Context, ev: friends | connEvent) -> StopEvent:
        ready = ctx.collect_events(ev,[friends,connEvent])
        if (ready == None):
            print("Awaiting events")
        else:
            print("Events ready!")
            conn.execute(text(f"select * from friends where fid = {ctx.data["regno"]};"))

async def main():
    f= friendsFlow(timeout=10, verbose=0)
    res = await f.run()
    print(res)

if __name__ == '__main__':
    asyncio.run(main())

