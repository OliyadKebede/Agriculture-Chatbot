import inspect, os


def getModelPath():
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.path.join(path, 'models/nlu-20230320-190730-simple-set.tar.gz').replace("\\", "/")
    return path

def getJsonPath():
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.path.join(path, 'rasa_dataset.json').replace("\\", "/")
    return path

def getPath(file):
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.path.join(path, file).replace("\\", "/")
    return path
