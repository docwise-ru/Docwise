import uvicorn

from fastapi import FastAPI
from app.api.routes.auth import router as auth_router
from app.api.routes.auth import auth

app = FastAPI()
app.include_router(auth_router)

auth.handle_errors(app)

if __name__ == '__main__':
    uvicorn.run("app.main:app", host='127.0.0.1', port=8000, reload=True)
