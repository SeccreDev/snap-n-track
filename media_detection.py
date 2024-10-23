import cv2
def snap_track(file_path):
    # -----DNN MODEL----- #
    # Model architecture
    prototext = "model/MobileNetSSD_deploy.prototxt.txt"

    # Model Weights
    model = "model/MobileNetSSD_deploy.caffemodel"

    # Class Labels
    classes = {0:"background", 1:"aeroplane", 2:"bicycle", 3:"bird", 4:"boat", 5:"bottle", 6:"bus", 7:"car", 8:"cat", 9:"chair",
               10:"cow", 11:"dining-table", 12:"dog", 13:"horse", 14:"motorbike",  15:"human", 16:"potted-plant", 17:"sheep",
               18:"sofa", 19:"train", 20:"tv-monitor"}

    # Load the model
    net = cv2.dnn.readNetFromCaffe(prototext, model)

    # -----READ MEDIA-----
    # ---IMAGE---
    if any(x in file_path for x in [".jpg", ".jpeg", ".png"]):
        media = cv2.imread(file_path)

        process_media(classes, net, media)

        cv2.imshow("Image", media)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # ---VIDEO---
    else:
        cap = cv2.VideoCapture(file_path)

        # Check if video file opened successfully
        while cap.isOpened():
            ret, media  = cap.read()

            # if frame is read correctly ret is TRUE
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            process_media(classes, net, media)

            cv2.imshow("Video", media)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

def process_media(classes, net, media):
    # -----PREPROCESSING-----
    height, width, _ = media.shape
    frame_resized = cv2.resize(media, (300, 300))

    # -----BLOB CREATION-----
    blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5))

    # -----DETECTION & PREDICTION-----
    net.setInput(blob)
    detection = net.forward()

    for detection in detection[0][0]:
        # detection[2] is the confidence level
        if detection[2] > 0.40:
            label = classes[detection[1]]
            box = detection[3:7] * [width, height, width, height]
            x_start, y_start, x_end, y_end = int(box[0]), int(box[1]), int(box[2]), int(box[3])
            cv2.rectangle(media, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
            cv2.putText(media, "Conf: {:.2f}".format(detection[2] * 100), (x_start, y_start - 5), 1, 1.2, (255, 255, 255), 2)
            cv2.putText(media, label, (x_start, y_start - 20), 1, 1, (255, 255, 255), 2)