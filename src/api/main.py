from fastapi import FastAPI
from presentation.controllers.user_controller import user_controller
from presentation.controllers.conversation_controller import conversation_controller
from infrastructure.config.db import init_models

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(conversation_controller.router)

@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.on_event("startup")
async def on_startup():
    await init_models() 