from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome")
def welcome():
    return{
        "massage" : "Hello from welcome function in the code"
    }