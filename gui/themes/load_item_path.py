from genericpath import isfile
import os

from .theme_switch import Theme_Switch

class Load_Item_Path():
    cwd_path = os.path.abspath(os.getcwd())
    dir_path = os.path.join(cwd_path,"gui/themes")
    switch = Theme_Switch().switch["switch_theme"]
    theme_path = os.path.join(cwd_path, dir_path, switch)
    
    
    def isfile_exist_decorator(func): 
        def decorated(self, item_name):
            if "svg_icon" in func.__name__:
                item_dir_name = "svg_icons" 
            elif "svg_image" in func.__name__:
                item_dir_name = "svg_images" 
            elif "icon" in func.__name__:
                item_dir_name = "icons" 
            elif "image" in func.__name__:
                item_dir_name = "images" 
            item_path = os.path.normpath(os.path.join(Load_Item_Path.theme_path, "images", item_dir_name, item_name))
            
            if os.path.isfile(item_path):
                pass
            else:
                Load_Item_Path.theme_path = os.path.join(Load_Item_Path.dir_path, "default")
            return func(self, item_name)
            
        return decorated

    # Based on theme icon path
    @isfile_exist_decorator
    def set_icon_path(self, icon_name):
        icon_path = os.path.normpath(
            os.path.join(Load_Item_Path.theme_path, "images/icons", icon_name)
        )
        return icon_path
    
    @isfile_exist_decorator
    def set_svg_icon_path(self, icon_name):
        icon_path = os.path.normpath(
            os.path.join(Load_Item_Path.theme_path, "images/svg_icons", icon_name)
        )
        return icon_path
    
    @isfile_exist_decorator
    def set_image_path(self, image_name):
        image_path = os.path.normpath(
            os.path.join(Load_Item_Path.theme_path, "images/images", image_name)
        )
        return image_path
    
    @isfile_exist_decorator
    def set_svg_image_path(self, image_name):
        image_path = os.path.normpath(
            os.path.join(Load_Item_Path.theme_path, "images/svg_images", image_name)
        )
        return image_path
    