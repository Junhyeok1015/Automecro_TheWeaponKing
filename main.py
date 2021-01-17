import pyautogui as pag
import mss, cv2
import numpy as np

pag.PAUSE = 0.08

#bluestacks
# icon position
# set coordination manually
left_icon_pos = {'left':100, 'top': 540, 'width': 70, 'height': 70}
right_icon_pos = {'left': 250, 'top': 540, 'width': 70, 'height':70}

#button position
# set coordination manually
left_button = [69, 669]
right_button = [354, 667]

# verify icons
def compute_icon_type(img):
    # mean of RGB channel
    mean = np.mean(img, axis = (0, 1))
    # reset result
    result = None

    if mean[0] > 50 and mean[0] < 55 and mean[1] > 50 and mean[1] < 55 and mean[2] > 50 and mean[2] < 55:
        result = 'BOMB'
    elif mean[0] > 250 and mean[1] > 85 and mean[1] < 110 and mean[2] > 250:
        result = 'SWORD'
    elif mean[0] > 100 and mean[0] < 130 and mean[1] > 150 and mean[1] < 200 and mean[2] > 90 and mean[2] < 110:
        result = 'POISON'
    elif mean[0] > 210 and mean[0] < 230 and mean[1] > 200 and mean[1] < 225 and mean[2] > 120 and mean[2] < 135:
        result = 'JEWEL'

    return result

# click function
def click(coords):
    pag.moveTo(x=coords[0], y=coords[1], duration= 0.0)
    pag.mouseDown()
    pag.mouseUp()

while True:
    # capture image
    with mss.mss() as sct:
        left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
        right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]

        # cv2.imshow('left_img', left_img)
        # cv2.imshow('right_img', right_img)
        # cv2.waitKey(0)

        left_icon = compute_icon_type(left_img)
        right_icon = compute_icon_type(right_img)

        if left_icon == 'SWORD' and (right_icon == 'BOMB' or right_icon == 'POISON'):
            print('TAP LEFT!')
            click(left_button)
        elif right_icon =='SWORD' and (left_icon == 'BOMB' or left_icon == 'POISON'):
            print("TAP RIGHT!")
            click(right_button)
        elif left_icon == 'JEWEL' and right_icon == 'JEWEL':
            print("FEVER!")
            click(left_button)
            click(right_button)
        else:
            continue

    
