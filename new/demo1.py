
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
class demo:

    # def print_name(name):
    #     logging.info(f'name is {name}')
    def add_no(n1,n2):
        logging.info('ans is ',int(n1)+int(n2))
   