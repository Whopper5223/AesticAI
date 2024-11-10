import tensorflow as tf
from object_detection.utils import label_map_util
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Set paths to model and label map
model_path = "C:/Users/m20mi/Documents/Work/Aestic/Savior/saved_model"
label_map_path = "C:/Users/m20mi/Documents/Work/Aestic/skin_label_map.pbtxt"
image_path = "C:/Users/m20mi/Documents/Work/Aestic/Data/01F3MMXJ24BWB58NHE1QVGMZJ3_jpeg_jpg.rf.28ed2e6fcdb3069e121c7970d5d679bc.jpg"  # Path to the image you want to run inference on

# Load the trained model
detect_fn = tf.saved_model.load(model_path)

# Load the label map to translate class IDs to names
category_index = label_map_util.create_category_index_from_labelmap(label_map_path, use_display_name=True)

# Load an image and convert to tensor
image = cv2.imread(image_path)
image = cv2.resize(image, (300, 300))
input_tensor = tf.convert_to_tensor(image)
input_tensor = input_tensor[tf.newaxis, ...]

# Perform inference
detections = detect_fn(input_tensor)

# Extract detection data
detection_boxes = detections['detection_boxes'][0].numpy()  # Bounding boxes
detection_classes = detections['detection_classes'][0].numpy().astype(int)  # Class IDs
detection_scores = detections['detection_scores'][0].numpy()  # Confidence scores

# Copy image for drawing
image_with_detections = image.copy()

# Set a confidence threshold and max boxes to draw
confidence_threshold = 0.3  # Increase this threshold to filter low-confidence detections
max_boxes_to_draw = 10000  # Limit the number of boxes to avoid clutter

# List to store detection results
detection_results = []

# Draw bounding boxes and labels on the image
for i in range(min(len(detection_scores), max_boxes_to_draw)):
    if detection_scores[i] >= confidence_threshold:
        # Get bounding box coordinates and class label
        box = detection_boxes[i]
        class_id = detection_classes[i]
        score = detection_scores[i]

        # Convert normalized bounding box to pixel coordinates
        h, w, _ = image.shape
        y_min, x_min, y_max, x_max = (box * [h, w, h, w]).astype(int)

        # Get label name from class ID
        label = category_index[class_id]['name']
        label_with_score = f"{label}: {score:.2f}"

        # Store detection information in the list
        detection_results.append({
            'label': label,
            'confidence': score,
            'box': [x_min, y_min, x_max, y_max]
        })

        # Draw bounding box
        cv2.rectangle(image_with_detections, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        # Draw label
        cv2.putText(image_with_detections, label_with_score, (x_min, y_min - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the resulting image with detections
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image_with_detections, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Print the detection results
print("Detected Objects:")
for result in detection_results:
    print(f"Label: {result['label']}, Confidence: {result['confidence']:.2f}, "
          f"Box: {result['box']}")
