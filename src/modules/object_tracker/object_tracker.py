from ultralytics import YOLO

model = YOLO('yolov8n.yaml').load('yolov8n.pt')

def main():
    results = model.train()

if __name__ == '__main__':
    main()