import logging
logging.basicConfig(filename='app.log' , format='%(asctime)s | %(levelname)s: %(message)s', level=logging.INFO)
logging.info('Hello, world!')