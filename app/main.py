from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello everyone. This is Shashank!"}

@app.get("/health")
def health():
    return {"status": "ok"}
