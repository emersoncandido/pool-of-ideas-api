from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"placeholder": "Pool of Ideas API"}

@app.get("/workflows")
def read_root():
    return {"message": "Testing workflows on GitHub Action"}
