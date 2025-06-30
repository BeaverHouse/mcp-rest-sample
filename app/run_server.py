import uvicorn
import os

# Custom module import
from server import app

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", 8001)
    uvicorn.run(app, host=host, port=port)