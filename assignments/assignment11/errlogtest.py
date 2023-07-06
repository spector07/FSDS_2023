# 11. Create a Python program that logs an error message to the console and a file named
# "errors.log" if an exception occurs during the program's execution. The error
# message should include the exception type and a timestamp



import logging
logging.basicConfig(filename='error.log' , format='%(asctime)s | %(levelname)s: %(message)s', level=logging.INFO)


class CustomException(Exception):
    pass

try:
    a = int(input("Please enter a number: "))
    b = int(input("Please enter a number: "))
    c = a/b
    logging.info(f'Result is ${c}')
except Exception as e:
    logging.error(e)