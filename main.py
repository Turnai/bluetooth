import bluetooth
import time
import ctypes

if __name__ == '__main__':
    devices = {}

    for _ in range(3):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("Found {} devices.".format(len(nearby_devices)))
        for addr, name in nearby_devices:
            devices[addr] = name
        time.sleep(5)

    for addr, name in devices.items():
        print("  {} - {}".format(addr, name))

    if "" in devices.values():
        print("matched!")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\PycharmProjects\\bluetooth\\bg1.jpg", 0)
    else:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\PycharmProjects\\bluetooth\\bg2.jpg", 0)
