from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.endpoints import router

app = FastAPI()

# Include the API router
app.include_router(router=router, prefix="/api")

host = "localhost"
port = 9000

@app.get("/")
async def root():
    return RedirectResponse(url=f"http://{host}:{port}/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=host, port=port)
