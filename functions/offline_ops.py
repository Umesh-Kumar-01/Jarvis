import pyautogui


def takeScreenShot(path):
    myScreenShot = pyautogui.screenshot()
    default_folder = r"C:\Users\umesh\Documents"
    if path != "":
        default_folder = path

    myScreenShot.save(default_folder)
    return


