import uiautomator2 as u2
import time
import random
import string

def create_username():
    return  'a' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

d = u2.connect("emulator-5558")

# ----------------------------------------------------------------
# start tools

element = d(text="一拳超人：最强之男")
if element.exists():
    element.click()
    d.implicitly_wait(70.0)

# # Dang ki acc
exit_signUp = d(resourceId = "com.flamingo.sdk:id/view_login_welcome_switch_account")
if(exit_signUp.exists()):
    exit_signUp.click()

sign_up = d(text="快速注册")

sign_up.click()

user_name = d(resourceId ="com.flamingo.sdk:id/view_register_user_name")
user_name.clear_text()
text = create_username()
f = open("data.txt", "w")
f.write(text)
f.close()
user_name.set_text(text)

password = d(resourceId ="com.flamingo.sdk:id/view_register_password")
password.clear_text()
password.set_text("Thuc12345")
checkbox = d(resourceId ="com.flamingo.sdk:id/view_protocol_checkbox")
checkbox.click()
verify = d(resourceId ="com.flamingo.sdk:id/view_register_commit")
verify.click()

# xac minh cmnd

identity_name = d(resourceId ="com.flamingo.sdk:id/view_dialog_verify_identity_name")
identity_name.set_text("蔡培初")

identity_num = d(resourceId ="com.flamingo.sdk:id/view_dialog_verify_identity_num")
identity_num.set_text("360311198512161574")

identity_commit = d(resourceId ="com.flamingo.sdk:id/view_dialog_verify_identity_commit")
identity_commit.click()

btnOk = d(resourceId ="com.flamingo.sdk:id/gp_sdk_save_pic_btn_know")
btnOk.click()

# xoa banner va vao game
today_no_more_notice = d(resourceId ="com.flamingo.sdk:id/today_no_more_notice")
today_no_more_notice.click_exists()

push_close = d(resourceId ="com.flamingo.sdk:id/push_close")
push_close.click_exists()

screen_size = d.window_size()

x = screen_size[1]*0.9
y= screen_size[0]*0.1
time.sleep(60)
d.click(x,y)

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
