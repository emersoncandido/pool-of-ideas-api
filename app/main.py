from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"placeholder": "Pool of Ideas API"}

@app.get("/workflow")
def read_workflow():
    return {"message": "New temporary endpoint"}
