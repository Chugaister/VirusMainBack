from uvicorn import run
from utils.config import config

if __name__ == "__main__":
    run(
        app="app:app",
        host=config.HOST,
        port=config.PORT,
        ssl_certfile=config.SSL_CERTFILE_PATH,
        ssl_keyfile=config.SSL_KEYFILE_PATH,
        ssl_ca_certs=config.SSL_CA_BUNDLE_FILE_PATH
    )