bl_info = {
    "name": "Project Folder Opener",
    "blender": (2, 80, 0),
    "category": "System",
    "description": "Quickly view the current file path in a file explorer window",
    "author": "Sören Schmidt-Clausen",
    "version": (1, 0),
    "location": "File > Project Folder",
}

import bpy
import os
import subprocess
from bpy.types import Operator
import sys

class OPEN_BLEND_FOLDER_OT_open_file_folder(Operator):
    bl_idname = "file.open_blend_folder"
    bl_label = "Project Folder"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ""

    def execute(self, context):
        filepath = bpy.data.filepath
        if filepath:
            folder_path = os.path.dirname(filepath)
            
            if os.name == 'nt':  # Windows
                os.startfile(folder_path)
            elif os.name == 'posix':  # macOS and Linux
                subprocess.Popen(['open' if sys.platform == 'darwin' else 'xdg-open', folder_path])
            # self.report({'INFO'}, "Folder opened: " + folder_path)
        else:
            self.report({'WARNING'}, "Save the blend file first!")
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator("file.open_blend_folder", icon="FOLDER_REDIRECT")

def register():
    bpy.utils.register_class(OPEN_BLEND_FOLDER_OT_open_file_folder)
    bpy.types.TOPBAR_MT_file.append(menu_func)

def unregister():
    bpy.types.TOPBAR_MT_file.remove(menu_func)
    bpy.utils.unregister_class(OPEN_BLEND_FOLDER_OT_open_file_folder)

if __name__ == "__main__":
    register()
