# _*_ encoding:utf-8 _*_

import os
os.chdir("../Plugins/ABSystem")
os.system("dir /b")
os.system("git pull")

print("Press any key to exit")
raw_input()