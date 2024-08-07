from ultralytics import YOLO

class Object_Tracker:

    model = YOLO('yolov8n.yaml').load('./yolo_models/yolov8n.pt')

    def __init__(self) -> None:
        self.source = None
    
    def setSource(self, source):
        self.source = source

    def track(self):
        if self.source is None:
            return -1;
        else:
            result =  self.model.track(source = self.source, show = True, tracker = "bytetrack.yaml")
            return result