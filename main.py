from uvicorn import run
from utils.config import config

if __name__ == "__main__":
    run(
        app="app:app",
        host=config.HOST,
        port=config.PORT
    )
