import os
import logging
import sys
sys.path.append('./assets')
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

def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = gui.MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()





