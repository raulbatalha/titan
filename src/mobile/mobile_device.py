import time
import xml.etree.ElementTree as ET
import subprocess


def get_devices():
    device_command = subprocess.Popen(
        "adb devices", shell=True, stdout=subprocess.PIPE).communicate()[0]
    output_device = str(device_command).split("attached")[1]
    output_device = output_device.split("device")[0]
    output_device = output_device.replace(
        "\\n", "").replace("\\t", "").replace("'", "")
    return output_device


def get_xml(serial):
    long_time = subprocess.Popen(
        "adb -s %s shell settings put system screen_off_timeout 600000", serial, shell=True, stdout=subprocess.PIPE).communicate()[0]
    device_command = subprocess.Popen("adb -s %s shell uiautomator dump" %
                                      serial, shell=True, stdout=subprocess.PIPE).communicate()[0]
    device_command = subprocess.Popen("adb -s %s pull /sdcard/window_dump.xml ./src/mobile/xml" %
                                      serial, shell=True, stdout=subprocess.PIPE).communicate()[0]


def tap_screen(app_name, x, y):
    device_command = subprocess.Popen("adb shell input tap %s %s" % (
        x, y), shell=True, stdout=subprocess.PIPE)
    time.sleep(5)


def get_screen(serial):
    device_command = subprocess.Popen("adb -s %s exec-out screencap -p > ./src/mobile/image/window_screen.png" %
                                      serial, shell=True, stdout=subprocess.PIPE).communicate()[0]
    time.sleep(5)


def touch_screen(node, app_name):
    if node.attrib.get('text') == app_name:
        position = node.attrib.get('bounds').split(']')[0]
        position = position.replace("[", "").split(",")
        tap_screen(app_name, position[0], position[1])
    else:
        for n in node.findall('node'):
            touch_screen(n, app_name)


def click_element(name_text):
    xml = ET.parse('./src/mobile/xml/window_dump.xml')
    root = xml.getroot()
    app = touch_screen(root, name_text)


def getprop_model(serial):
    device_command = subprocess.Popen("adb -s %s shell getprop ro.product.model" %
                                      serial, shell=True, stdout=subprocess.PIPE).communicate()[0]
    with open('./src/mobile/txt/model.txt', 'wb') as file:
        file.write(device_command)

    with open('./src/mobile/txt/model.txt', 'r') as file:
        line = file.readline()

    with open('./src/mobile/txt/model.txt', 'w') as file:
        for text_files in line:
            if text_files.strip("\n"):
                file.write(text_files)


print("Device:", get_devices())
getprop_model(get_devices())
get_xml(get_devices())
