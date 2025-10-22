from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello CI/CD World - Automated Deployment!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}