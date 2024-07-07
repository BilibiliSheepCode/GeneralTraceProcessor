import os
import logging
import sys
import time

log_path = "./log"
data_path = "./data"
modules_path = "./modules"
cam_path = modules_path + "/cam"
gui_path = modules_path + "/gui"
trace_path = modules_path + "/trace"
log_file_path = log_path + "/" + time.asctime().replace(' ', '-').replace('--', '-').replace(':', '-') + '.log'

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_file = logging.FileHandler(log_file_path)
handler_stream = logging.StreamHandler(sys.stdout)
handler_file.setFormatter(formatter)
handler_stream.setFormatter(formatter)
logger.addHandler(handler_file)
logger.addHandler(handler_stream)
logger.setLevel(logging.INFO)

def createNewProject():
    name = input("Project Name: ")
    while os.path.exists(data_path + '/' + name):
        name = input("Project Existed!\nEnter New Project Name: ")
    project_path = data_path + '/' + name
    os.mkdir(project_path)
    os.mkdir(project_path + '/traceData')
    os.mkdir(project_path + '/operates')
    open(project_path + '/config.yml', "w").close()
    

def main():
    traceDatas = os.listdir(data_path)

    if len(traceDatas) == 0:
        logger.info("Creating New Trace Project.")
        createNewProject()
    else:
        pass

if __name__ == "__main__":
    main()





