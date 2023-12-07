"""Main Pool of Ideas API endpoints"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"placeholder": "Pool of Ideas API"}

@app.get("/workflow")
def read_workflow():
    """Temporary endpoint"""
    return {"message": "New temporary endpoint"}
