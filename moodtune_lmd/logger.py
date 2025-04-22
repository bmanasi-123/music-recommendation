import logging


logger = logging.getLogger("moodtune")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
