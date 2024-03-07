from src.api.main import app

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True, log_level="info")

