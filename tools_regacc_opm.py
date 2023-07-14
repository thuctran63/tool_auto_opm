import os
import cv2
import numpy as np
import uiautomator2 as u2
import time
import random
import string



def create_username():
    return  'a' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(11))

def check_image(image_check_path, image_source_path):
    image_check = cv2.imread(image_check_path,0)
    image_source = cv2.imread(image_source_path,0)
    
    result = cv2.matchTemplate(image_source, image_check, cv2.TM_CCOEFF_NORMED)
    
    threshold = 0.8
    
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    if locations:
        center_x = np.mean([x for x, y in locations])
        center_y = np.mean([y for x, y in locations])
        os.remove(image_source_path)
        return (center_x, center_y)
    else:
        return None
# ----------------------------------------------------------------
# start tool

def start_tool(emulator):
    
    d = u2.connect(emulator)
    screen_size = d.window_size()
    element = d(text="一拳超人：最强之男")
    if element.exists():
        element.click()

    switch_acc = d(resourceId = "com.flamingo.sdk:id/view_login_welcome_switch_account")
    user_name = d(resourceId ="com.flamingo.sdk:id/view_register_user_name")
    password = d(resourceId ="com.flamingo.sdk:id/view_register_password")
    checkbox = d(resourceId ="com.flamingo.sdk:id/view_protocol_checkbox")
    verify = d(resourceId ="com.flamingo.sdk:id/view_register_commit")
    sign_up = d(text= "快速注册")
    user_name = d(resourceId ="com.flamingo.sdk:id/view_register_user_name")
    identity_name = d(resourceId ="com.flamingo.sdk:id/view_dialog_verify_identity_name")
    identity_num = d(resourceId ="com.flamingo.sdk:id/view_dialog_verify_identity_num")
    identity_commit = d(resourceId ="com.flamingo.sdk:id/view_dialog_verify_identity_commit")
    btnOk = d(resourceId ="com.flamingo.sdk:id/gp_sdk_save_pic_btn_know")
    today_no_more_notice = d(resourceId ="com.flamingo.sdk:id/today_no_more_notice")
    push_close = d(resourceId ="com.flamingo.sdk:id/push_close")
    
    time.sleep(5)
    while True:
        start_time = time.time()
        if(switch_acc.exists()):
            try:
                switch_acc.click()
                break
            except:
                time.sleep(3)
                pass
        
    while True:
        if(sign_up.exists()):
            try:
                sign_up.click()
                user_name.clear_text()
                text = create_username()
                with open("Tools_game_OPM/data.txt", "a") as f:
                    f.write(text + '\n')
                user_name.set_text(text)
                password.clear_text()
                password.set_text("Thuc12345")
                checkbox.click()
                verify.click()
                break
            except:
                time.sleep(1)
                pass

    while True:
        start_time = time.time()
        if(identity_name.exists()):
            try:
                identity_name.set_text("蔡培初")
                identity_num.set_text("360311198512161574")
                identity_commit.click()
                btnOk.click()
                break
            except:
                time.sleep(1)
                pass

    while True:
        time_start = time.time()
        if(push_close.exists()):
            try:
                today_no_more_notice.click_exists()
                push_close.click_exists()
                break
            except:
                time.sleep(1)
                pass
    
    while True:
        try:
            pic = d.screenshot()
            pic.save("Tools_game_OPM/image/abd.png")
            location = check_image("Tools_game_OPM/image/exit.png","Tools_game_OPM/image/abd.png")
            x = location[0]
            y= location[1]
            d.click(x,y)
            break
        except:
            time.sleep(1)
            pass

    x = screen_size[1]*0.5
    y = screen_size[0]*0.69
    time.sleep(3)
    d.click(x,y)

    x = screen_size[1]*0.4
    y = screen_size[0]*0.3
    time.sleep(3)
    d.click(x,y)

    y = screen_size[0]*0.8
    x = screen_size[1]*0.5
    time.sleep(3)
    d.click(x,y)


