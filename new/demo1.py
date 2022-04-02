
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
logging_str="[%(asctime)s:%(levelname)s:%(module)s]%(message)"
logging.basicConfig(level=logging.INFO,format=logging_str)
def print_name(name):
    logging.info(f'name is {name}')
def add_no(n1,n2):
    logging.info(f'final ans is {n1}+{n2}')
   