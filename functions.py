import re
import urllib.request
import webbrowser

import pyautogui
import requests
import urllib3


def greetHelloInRandomLang():
    """
    Returns a string having random greeting message.
    Returns:
        string: greet message
    """
    response = requests.get("https://www.greetingsapi.com/random")
    json_data = response.json()
    # print(json_data)
    return json_data['greeting'] + "! That's hello in " + json_data["language"]


def playMusicOnYoutube(data):
    """
    This function will play music on YouTube using WebBrowser module.
    Args:
        data: name of music or the video name which you want to search on YouTube

    Returns:

    """
    d = data.split(" ")
    data = "+".join(d)

    search = "https://www.youtube.com/results?search_query=" + data
    html = urllib.request.urlopen(search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    final_link = "https://www.youtube.com/watch?v="
    final_link += video_ids[0]

    webbrowser.open(final_link)


def takeScreenShot(path):
    myScreenShot = pyautogui.screenshot()
    default_folder = r"C:\Users\umesh\Documents"
    if path != "":
        default_folder = path

    myScreenShot.save(default_folder)
    return


if __name__ == '__main__':
    test = greetHelloInRandomLang()
    print(test)
    playMusicOnYoutube("kusu kusu")
