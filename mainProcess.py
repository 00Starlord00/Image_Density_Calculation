import os
from imageai.Detection import ObjectDetection
import tensorflow
import keras

def crowdCount(input_image):
    '''
    Paths
    execution_path : Path of directory where the models are saved
    inpput_path : Django media path
    output_path : Django media path
    '''
    execution_path= 'C:\\Users\\Pranav\\Documents\\Projects\\FinalYear\\Models'
    input_path= 'C:\\Users\\Pranav\\Documents\\Projects\\FinalYear\\FrontEnd\\media'
    output_path= 'C:\\Users\\Pranav\\Documents\\Projects\\FinalYear\\FrontEnd\\media'
    
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    
    output_image = '_'.join(["output", input_image])
    objects_present = detector.CustomObjects(person = True)
    detections = detector.detectCustomObjectsFromImage(
                    custom_objects = objects_present, 
                    input_image = os.path.join(input_path, input_image), 
                    output_image_path = os.path.join(output_path, output_image), 
                    minimum_percentage_probability = 29)
    people_count = len(detections)
    
    return people_count, output_image



'''
input_image = 'IMG_1.jpg'
total_count = crowdCount(input_image)
print('Number of people: ', total_count)
'''