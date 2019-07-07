import platform

def isWindowsSystem():
    return 'Windows' in platform.system()

def isLinuxSystem():
    return 'Linux' in platform.system()

def system():
    if 'Windows' in platform.system():
        return 'Windows'
    if 'Linux' in platform.system():
        return 'Linux'
    return None

if __name__ == '__main__':
    if isWindowsSystem():
        if not isLinuxSystem():
            print('win')
    if isLinuxSystem():
        if not isWindowsSystem():
            print('linux')
    print(system())