# H0lygh0st Simulator
# Generates IOCs for EDR to pick up
# Author: Tyler Hardy
# Requires Python 3.x
# Operating System: Windows NT or Linux/Mac

import os
import time


def encrypt(path_enc, length_of_time):
    """
    Performs fake encryption of user's files
    :param path_enc: directory to rename contents of
    :param length_of_time: length of time, in seconds, to run the simulation
    :return: void
    """
    count = len(os.listdir(path_enc))
    print(count)
    dst = [None] * count
    src = [None] * count
    i = 0
    for count, filename in enumerate(os.listdir(path_enc)):
        print(filename)
        dst[i] = f"{path_enc}/{filename}.h0lyenc"
        src[i] = f"{path_enc}/{filename}"
        print(dst[i])
        print(src[i])
        os.rename(src[i], dst[i])
        i = i + 1

    f = open(f"{path_enc}/FOR_DECRYPT.html", "w")
    f.write("<html><h1>H0lyGh0st\n</h1><h2>Please Read this text to decrypt all files encrypted.\n</h2>"
            "<h3>Don't worry, you can return all of your files.\n</h3>"
            "<h3>If you want to restore all of your files, Send mail to <u>H0lyGh0st@mail2tor.com</u> with your Id. Your ID is -\n</h3>"
            "<h1>KAROLISLIUC875C</h1>"
            "<h3>Or install tor browser and contact us with your id or company name(If all of pcs in your company are encrypted).</h3>"
            "<h3>Our site : H0lyGh0stWebsite\n\n\nOur Service\n</h3>"
            "<h3>After you pay, We will send unlocker with decryption key\n</h3>"
            "<h1>Attention!\n</h1>"
            "<h2>1. Do not rename encrypted files.\n</h2>"
            "<h2>2. Do not try to decrypt your data using third party software, it may cause permanent data loss.\n</h2>"
            "<h2>3. Decryption of your files with the help of third parties may cause increase price.\n</h2>"
            "<h2>4. Antivirus may block our unlocker, So disable antivirus first and execute unlocker with decryption key.\n</h2>")
    f.close()

    time.sleep(int(length_of_time))
    for n in range(i):
        os.rename(dst[n], src[n])

    if os.path.exists(f"{path_enc}/FOR_DECRYPT.html"):
        os.remove(f"{path_enc}/FOR_DECRYPT.html")
    else:
        print("Someone removed the decryptor file")



if __name__ == '__main__':
    """
    Handle running as a script
    """
    if os.environ.get('OS', '') == 'Windows_NT':
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    else:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)
    #test = r"C:/Users/thardy/Desktop/test"
    time_length = 60
    encrypt(desktop, time_length)
