# _*_ coding:UTF-8 _*_
# 拷贝工程用到的一些第三方库

import os
import shutil

# dll path
path_Unity3DGameLib = r'../Plugins/Unity3DGameLib/Unity3DGameLib/bin/Debug/Unity3DGameLib.dll'
path_Unity3DGameLibEditor = r'../Plugins/Unity3DGameLib/Unity3DGameLibEditor/bin/Debug/Unity3DGameLibEditor.dll'

# target path
target_Unity3DGameLibPath = r'../WarX_Client/Assets/Plugins/Unity3DGameLib.dll'
target_Unity3DGameLibEditorPath = r'../WarX_Client/Assets/Plugins/Editor/Unity3DGameLibEditor.dll'

if os.path.exists(path_Unity3DGameLib):
    print("Copy Unity3DGameLib.dll")
    shutil.copyfile(path_Unity3DGameLib,target_Unity3DGameLibPath)
else:
    print("Unity3DGameLib.dll not exists")


if os.path.exists(path_Unity3DGameLibEditor):
    print("Copy Unity3DGameLibEditor.dll")
    shutil.copyfile(path_Unity3DGameLibEditor,target_Unity3DGameLibEditorPath)
else:
    print("Unity3DGameLibEditor.dll not exists")


absystem_source_path = r'../Plugins/ABSystem/Assets/ABSystem'
absystem_target_path = r'../WarX_Client/Assets/Plugins/ABSystem'

if(os.path.exists(absystem_target_path)):
    print("Delete old ABSystem")
    shutil.rmtree(absystem_target_path)

print("Copy new ABSystem")
shutil.copytree(absystem_source_path,absystem_target_path,False)
raw_input()
raw_input()