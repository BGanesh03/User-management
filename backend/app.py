from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from controllers import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=5000, reload=True)