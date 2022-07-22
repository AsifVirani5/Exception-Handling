import logging
logging.basicConfig(filename = 'Oops3.log', level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(message)s')

class person:

        def __init__(self, name, surname, emailid):
            try:cd
                self.name = name
                self.surname = surname
                self.emailid = emailid
                logging.info("This code is Oops code")
            except Exception as e:
                logging.exception(e)
                logging.info("This is been executed")
            finally:
                logging.info("this will be executed finally")

anuj1 = person('anuj', 'john', 'anuj9263@gmail.com')
print(anuj1.name)
print(anuj1.surname)
print(anuj1.emailid)











































