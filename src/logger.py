import logging
from datetime import datetime
import os


log_file_name = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'
log_path = os.path.join(os.getcwd(),'Logs',log_file_name)
os.makedirs(log_path,exist_ok=True)

log_file_path = os.path.join(log_path,log_file_name)

logging.basicConfig(
    filename=log_file_path, 
    level=logging.INFO, 
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)




if __name__ == "__main__":
    logging.info("Starting logger")




    


