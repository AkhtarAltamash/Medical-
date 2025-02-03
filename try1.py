# # from ultralytics import YOLO
# # import cv2
# # import matplotlib.pyplot as plt

# # # Load the YOLOv10 model
# # model_path = 'D:\\Python Works Altamash\\yolov10\\yolov10n.pt'  # Path to your model
# # model = YOLO(model_path)

# # # Path to the image you want to test
# # image_path = 'C:\\Users\\Altamash\\Downloads\\bt1.jpg'  # Update with your image path

# # # Perform inference
# # results = model(image_path)

# # # Print results
# # print("Inference Results:")
# # for result in results:
# #     print(result)

# # # Display the image with bounding boxes (only if detections exist)
# # if results:
# #     results[0].show()  # Displaying the first result's detections
# # else:
# #     print("No detections found.")

# # # If you want to save the result image, uncomment the following line
# # # results[0].save('D:\\Python Works Altamash\\yolov10\\output.jpg')  # Specify the output path
# # _________________________________________


# from ultralytics import YOLO
# import cv2
# import matplotlib.pyplot as plt

# # Load the YOLOv10 model
# model_path = 'D:\\Python Works Altamash\\yolov10\\yolov10n.pt'
# model = YOLO(model_path)

# # Path to the image with the tumor
# image_path = 'C:\\Users\\Altamash\\Downloads\\bt1.jpg'  # Your image path

# # Perform inference
# results = model(image_path)

# # Check and visualize results
# if results:
#     # Iterate over results to display
#     for result in results:
#         boxes = result.boxes  # Get the bounding boxes
#         if len(boxes) > 0:  # If there are boxes detected
#             # Display bounding boxes
#             img = cv2.imread(image_path)
#             for box in boxes.xyxy:  # Get box coordinates
#                 x1, y1, x2, y2, conf, cls = box  # Unpack the box
#                 cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)  # Draw rectangle
#                 cv2.putText(img, f'{model.names[int(cls)]} {conf:.2f}', (int(x1), int(y1)-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # Label
#             plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#             plt.axis('off')
#             plt.show()
#         else:
#             print("No detections found.")
# else:
#     print("Inference failed to return results.")



import cv2

# Load the image
image_path = r'D:\Python Works Altamash\brain tumor work\axial_t1wce_2_class\images\test\00018_101.jpg'
image = cv2.imread(image_path)

# Get the dimensions
if image is not None:
    height, width, channels = image.shape
    print(f"Width: {width}, Height: {height}")
else:
    print("Image not found or could not be loaded.")
