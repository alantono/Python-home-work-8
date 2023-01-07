import logging


def log(a):
    logging.basicConfig(filename="Phonebook.log", level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', encoding="utf-8")
    logging.info(a)
