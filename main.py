from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/")
def read_root():
    return { "200" : "Welcome"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)