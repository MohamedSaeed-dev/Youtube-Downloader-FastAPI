from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.endpoints import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
# Include the API router
app.include_router(router=router, prefix="/api")

host = "0.0.0.0"
port = 9000

# @app.get("/")
# async def root():
#     return RedirectResponse(url=f"http://{host}:{port}/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=host, port=port)
