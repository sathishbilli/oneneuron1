
def demo(df):
    #doc string
    """"
        demo doc string

    Args:

        df (int): it is a demo function

    Returns: 
        int
        demou
    """
import logging
logging_str="[%(asctime)s:%(levelname)s:%(module)s] %(message)s"
logging.basicConfig(level=logging.INFO,format=logging_str)
print()
logging.info("this a print name function")


    # def print_name(name):
    #     logging.info(f'name is {name}')
try:
    logging.info("________________________ strarting fun  ______________________________")
    def add_no(n1,n2):
        logging.info('ans is ',int(n1)/int(n2))
    logging.info("________________________ stop fun  ______________________________")
except Exception as e:
    logging.exception(e)
   