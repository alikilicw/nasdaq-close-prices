from fastapi import FastAPI
from fastapi.responses import JSONResponse
from main_service import main_service

# https://docs.google.com/spreadsheets/d/1_DReqeQ5haLU_CNjYo-t9tclTaCaE40tYkkIvocnvtQ/edit?gid=0#gid=0

app = FastAPI()

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