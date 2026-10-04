from fastapi import FastAPI
import uvicorn
import socket

app = FastAPI()

@app.get("/")
def read_root():
    hostname = socket.gethostname()
    return {
        "message": "Hello depuis Kubernetes !",
        "pod_name": hostname
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)