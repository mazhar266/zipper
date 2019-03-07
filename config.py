import os

SETTINGS = {
    "INFO": {
        "name": "zipper",
        "info": "The zipping micro-service",
        "version": "1.0.0",
    },
    "BASE_URL": "http://localhost:5000",

    "ZIP_DIR": os.path.basename('zips'),
    "CACHE_FOLDER": os.path.basename('cache'),
}
