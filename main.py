from fastapi import FastAPI
from fastapi.responses import JSONResponse
from main_service import main_service
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import timezone
from constants import SCHEDULER_HOUR, SCHEDULER_MINUTE
import time

# https://docs.google.com/spreadsheets/d/1_DReqeQ5haLU_CNjYo-t9tclTaCaE40tYkkIvocnvtQ/edit?gid=0#gid=0

scheduler = BackgroundScheduler()

def my_scheduled_task():
    print(f'Scheduled task executed: {time.strftime('%Y-%m-%d %H:%M:%S')}')
    main_service()

def start_scheduler():
    scheduler.add_job(my_scheduled_task, 'cron', hour=SCHEDULER_HOUR, minute=SCHEDULER_MINUTE, day_of_week='0,1,2,3,4,5', timezone=timezone('UTC'))
    scheduler.start()

def shutdown_scheduler():
    scheduler.shutdown()

app = FastAPI(
    on_startup = [start_scheduler],
    on_shutdown = [shutdown_scheduler]
)

@app.get('/index')
async def index():

    try:

        main_service()
        
        return JSONResponse(content={'message': 'OK.'}, status_code=200)
    
    except Exception as e:
        print(e)
        return JSONResponse(content={'error': str(e)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")