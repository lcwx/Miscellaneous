import cv2 as cv
import math

im = cv.imread("test.jpg")
# cv.rectangle(im, (10, 10), (110, 110), (0, 0, 255), thickness=1)
# cv.line(im, (20, 30), (40, 50), (0, 0, 255))

# print(math.tan(math.pi/4.0))
# k = 1.0 / math.tan(math.pi * ((90.0 + 45.0)/180.0))
# print(k)


def drawOffsetRec(im, leftupCoor, rightdownCoor, color, offset, thickness=1):
    # offset is °
    
    k = 1.0/math.tan(math.pi * ((90.0 - offset)/180.0))

    x_ld = (((k * leftupCoor[0] - leftupCoor[1]) +
             (rightdownCoor[0]/k + rightdownCoor[1])))/(k + 1.0/k)
    y_ld = k * x_ld - k * leftupCoor[0] + leftupCoor[1]

    x_ru = ((leftupCoor[0]/k + leftupCoor[1]) +
            (k * rightdownCoor[0] - rightdownCoor[1]))/(k + 1.0/k)
    y_ru = k * (x_ru - rightdownCoor[0]) + rightdownCoor[1]

    x_ld = int(x_ld)
    y_ld = int(y_ld)
    x_ru = int(x_ru)
    y_ru = int(y_ru)

    # print(type(leftupCoor))
    # print(type(rightdownCoor))
    # print(type(color))

    cv.line(im, leftupCoor, (x_ld, y_ld), color, thickness)
    cv.line(im, leftupCoor, (x_ru, y_ru), color, thickness)
    cv.line(im, rightdownCoor, (x_ru, y_ru), color, thickness)
    cv.line(im, rightdownCoor, (x_ld, y_ld), color, thickness)

    return im


im = drawOffsetRec(im, (10, 10), (160, 310), (0, 0, 255), 20.0)
cv.imshow("test", im)
cv.waitKey(0)
cv.destroyAllWindows()
