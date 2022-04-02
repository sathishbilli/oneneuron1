
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
import os
from tqdm import tqdm
logging_dir="log"
os.makedirs(logging_dir,exist_ok=True)
logging_str="[%(asctime)s:%(levelname)s:%(module)s] %(message)s"
logging.basicConfig(filename=os.path.join(logging_dir,"runnig_logs.log"),level=logging.INFO,format=logging_str)
print()
logging.info("this a print name function")


    # def print_name(name):
    #     logging.info(f'name is {name}')
try:
    logging.info("________________________ strarting fun  ______________________________")
    def add_no(n1):
        logging.info('ans is ', n1)
    logging.info("________________________ stop fun  ______________________________")
except Exception as e:
    logging.info("________________________ no is 0  ______________________________")
    logging.exception(e)
def run_for(name,no):
    for i in tqdm(range(0,no),total=no,desc='train model'):
        print(name,' ',i)