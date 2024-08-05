import os
import logging
import sys
import time
import yaml

from PySide6.QtWidgets import QApplication

from modules.gui import gui


# log_path = "./log"
# data_path = "./data"
# modules_path = "./modules"
# cam_path = modules_path + "/cam"
# gui_path = modules_path + "/gui"
# trace_path = modules_path + "/trace"
# log_file_path = log_path + "/" + time.asctime().replace(' ', '-').replace('--', '-').replace(':', '-') + '.log'
# config_file_path = "./config.yml"

# with open('config.yml', 'r') as file:
#     config = yaml.safe_load(file)

# logger = logging.getLogger(__name__)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler_stream = logging.StreamHandler(sys.stdout)
# handler_stream.setFormatter(formatter)
# logger.addHandler(handler_stream)
# logger.setLevel(logging.INFO)
# if config['file-log'] == True:
#     handler_file = logging.FileHandler(log_file_path)
#     handler_file.setFormatter(formatter)
#     logger.addHandler(handler_file)

# def createNewProject():
#     name = input("Project Name: ")
#     while os.path.exists(data_path + '/' + name):
#         name = input("Project Existed!\nEnter New Project Name: ")
#     project_path = data_path + '/' + name
#     os.mkdir(project_path)
#     os.mkdir(project_path + '/traceData')
#     os.mkdir(project_path + '/operates')
#     open(project_path + '/config.yml', "w").close()

def main():
    # traceDatas = os.listdir(data_path)

    # if len(traceDatas) == 0:
    #     logger.info("Creating New Trace Project.")
    #     createNewProject()
    # else:
    #     pass

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = gui.MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()





