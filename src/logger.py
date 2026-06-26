from datetime import datetime

def write_log(message):

    with open("../logs/error_log.txt","a") as file:

        file.write(
            f"{datetime.now()} : {message}\n"
        )