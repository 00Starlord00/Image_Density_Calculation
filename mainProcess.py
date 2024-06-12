import os
from imageai.Detection import ObjectDetection
from imageai.Detection import VideoObjectDetection
import tensorflow
import keras

'''
For image
'''
def ObjectCoutImg(input_image):
    '''
    Paths
    execution_path : Path of directory where the models are saved
    inpput_path : Django media path
    output_path : Django media path
    '''
    execution_path= 'C:\\Users\\Pranav\\Documents\\MS Program\\CSCI 264\\Project\\Models'
    input_path= 'C:\\Users\\Pranav\\Documents\\MS Program\\CSCI 264\\Project\\Object_detection\\media'
    output_path= 'C:\\Users\\Pranav\\Documents\\MS Program\\CSCI 264\\Project\\Object_detection\\media'

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    output_image = '_'.join(["output", input_image])
    detections = detector.detectObjectsFromImage(
                        input_image=os.path.join(input_path , input_image), 
                        output_image_path=os.path.join(output_path , output_image), 
                        minimum_percentage_probability=30)
    object_count = len(detections)
    obj_data_list = []
    for elem in detections:
        temp = []
        temp.append(elem["name"])
        temp.append(elem["box_points"])
        obj_data_list.append(temp)
    return object_count, obj_data_list, output_image

'''
For video
'''
def ObjectCoutVideo(input_video):
    '''
    Paths
    execution_path : Path of directory where the models are saved
    inpput_path : Django media path
    output_path : Django media path
    '''
    execution_path= 'C:\\Users\\Pranav\\Documents\\MS Program\\CSCI 264\\Project\\Models'
    input_path= 'C:\\Users\\Pranav\\Documents\\MS Program\\CSCI 264\\Project\\Object_detection\\media'
    output_path= 'C:\\Users\\Pranav\\Documents\\MS Program\\CSCI 264\\Project\\Object_detection\\media'

    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    content = []
    def app_content(count_arr):
        content.append(count_arr)

    def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
        app_content(count_arrays[-1])
    
    video_path = detector.detectObjectsFromVideo(
                    input_file_path=os.path.join(input_path, input_video),
                    output_file_path=os.path.join(output_path, "output_vid"),
                    save_detected_video = True,
                    frames_per_second=10,
                    per_second_function = forSeconds,
                    minimum_percentage_probability = 30)
    
    return video_path, content