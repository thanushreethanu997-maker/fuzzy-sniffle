import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def login(username):
    logging.info("Application started")

    if username:
        logging.info("User login successful")
    else:
        logging.warning("Username is empty")

def divide(a, b):
    try:
        result = a / b
        logging.info("Division successful")
        return result
    except ZeroDivisionError:
        logging.error("Cannot divide by zero")
        return None

# Run application
login("Thanushree")
divide(10, 2)
divide(10, 0)
logging.info("Application completed")