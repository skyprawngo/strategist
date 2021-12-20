import os

from .theme_switch import Theme_Switch

class Load_Item_Path():
    cwd_path = os.path.abspath(os.getcwd())
    app_path = "gui/themes"
    switch = Theme_Switch().switch["switch_theme"]

    def set_icon_path(self, icon_name):
        icon_path = os.path.normpath(
            os.path.join(self.cwd_path, self.app_path, self.switch, "images/icons", icon_name)
        )
        return icon_path
    
    def set_svg_icon_path(self, icon_name):
        icon_path = os.path.normpath(
            os.path.join(self.cwd_path, self.app_path, self.switch, "images/svg_icons", icon_name)
        )
        return icon_path
    
    def set_image_path(self, image_name):
        image_path = os.path.normpath(
            os.path.join(self.cwd_path, self.app_path, self.switch, "images/images", image_name)
        )
        return image_path
    
    def set_svg_image_path(self, image_name):
        image_path = os.path.normpath(
            os.path.join(self.cwd_path, self.app_path, self.switch, "images/svg_images", image_name)
        )
        return image_path