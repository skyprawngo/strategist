import os
import getpass

class Function_Login:
    def save_login_id(self, id):
        username = getpass.getuser()
        save_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist/user_data.txt"))
        with open(save_path, 'w') as datawriter:
            pass
        # learnpython 학습중
        
    