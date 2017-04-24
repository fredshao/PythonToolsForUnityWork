# _*_ coding:utf-8 _*_

import os
os.chdir("../Plugins/Unity3DGameLib")
os.system("git status")
os.system("git add .")
os.system("git status")

comment = raw_input("Enter Commit Message:")
if(comment == ''):
	comment = "Code Update"

commit_command = 'git commit -m "%s"' % (comment)
push_command = 'git push origin master'
os.system(commit_command)
os.system(push_command)

print("Press any key to exit")
raw_input()