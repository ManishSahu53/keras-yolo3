IMAGE_SIZE = 416
CLASSES = 'model_data/friends_classes.txt'
WEIGHTS = 'logs/final.h5'
ANCHORS = 'model_data/yolo_anchors.txt'
ANNOTATATIONS = 'model_data/annotation.txt'
LOGS = 'logs/000'
TINY_WEIGHTS = 'model_data/tiny_yolo_weights.h5'


# Parameters
SCORE = 0.6
IOU = 0.65
NUM_GPU = 1
EPOCH = 50
BATCH_SIZE = 8


# Mapping
MAPPING = {
    'joey': 0,
    'chandler':1,
    'ross':2,
    'monica':3,
    'rechal':4,
    'pheobe':5
}


FORMAT = ['.JPEG', '.JPG', '.PNG']