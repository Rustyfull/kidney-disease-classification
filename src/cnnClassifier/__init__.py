import os
import sys
import logging

logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"

log_dir = "logs"
os.makedirs(log_dir , exist_ok=True)

log_filepath = os.path.join(log_dir,"running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        # Schreibt in die Datei
        logging.FileHandler(log_filepath),
        # Schreibt gleichzeitig in die Konsole (stdout)
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("KidneyClassifier")

if __name__ == "__main__":
    logger.info("Logging-System erfolgreich initialisiert")