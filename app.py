import cv2
import numpy as np
import os
import track as t
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

brushThickness = 25
eraserThickness = 100

def main():
    folderPath = "Header"
    myList = os.listdir(folderPath)
    logger.info(f"Header images found: {myList}")

    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        if image is None:
            logger.error(f"Failed to load image: {imPath}")
            continue
        image = cv2.resize(image, (1280, 125))
        overlayList.append(image)
    
    if not overlayList:
        logger.error("No header images loaded")
        return
        
    logger.info(f"Loaded {len(overlayList)} header images")
    header = overlayList[0]
    drawColor = (255, 0, 255)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logger.error("Failed to open camera")
        return
        
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = t.handDetector(detectionCon=0.85)
    xp, yp = 0, 0
    imgCanvas = np.zeros((720, 1280, 3), np.uint8)
    
    try:
        while True:
            success, img = cap.read()
            if not success or img is None:
                logger.error("Failed to grab frame")
                break
                
            img = cv2.flip(img, 1)

            img = detector.findHands(img)
            lmList, bbox = detector.findPosition(img, draw=False)

            if len(lmList) >= 13:  # Ensure we have enough landmarks
                try:
                    x1, y1 = lmList[8][1:]
                    x2, y2 = lmList[12][1:]
                    
                    fingers = detector.fingersUp()
                    #logger.info(f"Fingers detected: {fingers}")
                    
                    if fingers[1] and fingers[2]:
                        xp, yp = 0, 0
                        print("Selection Mode")

                        if y1 < 125:
                            if 250 < x1 < 450:
                                header = overlayList[0]
                                drawColor = (255, 0, 255)
                            elif 550 < x1 < 750:
                                header = overlayList[1]
                                drawColor = (255, 0, 0)
                            elif 800 < x1 < 950:
                                header = overlayList[2]
                                drawColor = (0, 255, 0)
                            elif 1050 < x1 < 1200:
                                header = overlayList[3]
                                drawColor = (0, 0, 0)
                        cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)

                    if fingers[1] and fingers[2]==False:
                        cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
                        print("Drawing Mode")
                        if xp == 0 and yp == 0:
                            xp, yp = x1, y1

                        if drawColor == (0, 0, 0):
                            cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                            cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
                        else:
                            cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                            cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

                        xp, yp = x1, y1

         
                except (IndexError, TypeError) as e:
                    logger.error(f"Error processing landmarks: {e}")
                    continue
            

            img[0:125, 0:1280] = header
            img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
            cv2.imshow("Canvas", imgCanvas)
            cv2.imshow("Image", img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        logger.error(f"Error in main loop: {e}")
    finally:
        logger.info("Cleaning up resources...")
        cap.release()
        cv2.destroyAllWindows()
        logger.info("Cleanup complete")

if __name__ == "__main__":
    main()