from autost.api import *
import AbsPath

from Common.InfraLibAPI import *

WIFIName = ExternalDynamicConfig_getExternalWIFIName()
WIFIPassWord = ExternalDynamicConfig_getExternalWIFIPassWord()
screenName = ExternalConfig_getExternalDevicesName() + '-WIFI-' + 'WIFIDevice'

NumKeyboard = [
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
lowerLetterKeyboard = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
upperLettersKeyboard = [
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
specialNormalKeyboard = [
',', '!', '@', '$', '&', '^', '*', '()',
'.', '?', '#', '%', '&', '\\', '~', '|'
]
specialChineseKeyboard = [
'，', '！', '：', '@', '”“', "‘’", '（）',
'。', '？', '、', '……', '；', '~', '《》'
]

def belongToWhichKeyboard(keyboardname,word):
    isbelongto = False
    for i in range(0,len(keyboardname)):
        if word == keyboardname[i]:
            isbelongto = True
            break
    print('isbelongto==' + str(isbelongto))
    return isbelongto
 
def wordTransToImageName(word):
    imageName = word
    if word == '|':
        imageName = '与'
    elif word == '*':
        imageName = '乘号'
    elif word == ':':
        imageName = '冒号'
    elif word == '"':
        imageName = '双引号'
    elif word == '\\':
        imageName = '反斜杠'
    elif word == '>':
        imageName = '大于号'
    elif word == '<':
        imageName = '小于号'
    elif word == '/':
        imageName = '斜杠'
    elif word == '?':
        imageName = '问号'
    print('imageName==' + imageName)
    return imageName


def checkWIFIConnected():
    return poco(text=WIFIName, selected=True, timeout=3.0).exists()


def checkWIFINotConnected():
    return poco(text=WIFIName, selected=False, timeout=3.0).exists()


def connectWIFI():
    poco(text=WIFIName, timeout=3.0).click()


def assertWIFIConnected():
    poco(text=WIFIName, selected=True, timeout=3.0).assert_exists()


flick([960, 378], DIR_DOWN, step=1, speed=SPEED_NORMAL)
flick([960, 378], DIR_DOWN, step=1, speed=SPEED_NORMAL)

transToScreen("WiFi设定(WiFi打开并且热点关闭)画面")

if checkWIFIConnected():
    pass
else:    
    if checkWIFINotConnected():
        pass
    else:
        for i in range(0,3):
            flick([872, 203], DIR_DOWN, step=1, speed=SPEED_NORMAL)
            flick([872, 203], DIR_DOWN, step=1, speed=SPEED_NORMAL)
            for i in range(0,10):
                if checkWIFINotConnected():
                    break
                swipe([830,600], [830,310], duration=1)
 
            if  checkWIFINotConnected():
                break
    connectWIFI()
    if not checkExistPicture('连接网络密码输入画面',['keyboard返回按钮.png'],timeout=3):
        print('wifi is reconnecting')
    else:
        #输入密码
        #touch_if(Template('pic/讯飞画面_不再提示按钮.png'),timeout=5.0)
        #touch_if(Template('pic/同意按钮.png'),timeout=5.0)
        #touch_if(Template('pic/输入框.png'),threshold=0.90,timeout=5.0)
        if poco(text='允许').exists():
            for _ in range(3):
                if poco('允许', text='允许', timeout=1).exists():
                    poco('允许', text='允许').click()
                    sleep(0.5)
        clickPicture('连接网络密码输入画面',['讯飞画面_不再提示按钮.png'],timeout=5.0)
        clickPicture('连接网络密码输入画面',['同意按钮.png'],timeout=5.0)
        clickPicture('连接网络密码输入画面',['输入框.png'],threshold=0.90,timeout=5.0)
        for i in range(0, len(WIFIPassWord)) :
            print('password ' + str(i) + ' = ' + WIFIPassWord[i])
            if belongToWhichKeyboard(NumKeyboard,WIFIPassWord[i]):
                if checkExistPicture('连接网络密码输入画面',['返回按钮.png']):
                    print('is numkeyboard')
                else:
                    print('click 123按钮 switch to numkeyboard')
                    clickPicture('连接网络密码输入画面',['123按钮.png'])
                clickPicture('连接网络密码输入画面',[WIFIPassWord[i] + '.png'])
            elif belongToWhichKeyboard(lowerLetterKeyboard,WIFIPassWord[i]):
                if checkExistPicture('连接网络密码输入画面',['123按钮.png']):
                    pass
                else:
                    clickPicture('连接网络密码输入画面',['返回按钮.png'])
                if checkExistPicture('连接网络密码输入画面',['小写按钮.png']):
                    print('is lowerLetterKeyboard')
                else:
                    print('click 大写按钮 switch to lowerLetterKeyboard')
                    clickPicture('连接网络密码输入画面',['大写按钮.png'])
                clickPicture('连接网络密码输入画面',[WIFIPassWord[i] + '_lower.png'])
            elif belongToWhichKeyboard(upperLettersKeyboard,WIFIPassWord[i]):
                if checkExistPicture('连接网络密码输入画面',['123按钮.png']):
                    pass
                else:
                    clickPicture('连接网络密码输入画面',['返回按钮.png'])
                if checkExistPicture('连接网络密码输入画面',['大写按钮.png']):
                    print('is upperLettersKeyboard')
                else:
                    print('click 小写按钮 switch to upperLettersKeyboard')
                    clickPicture('连接网络密码输入画面',['小写按钮.png'])
                clickPicture('连接网络密码输入画面',[WIFIPassWord[i] + '_Upper.png'])
            elif belongToWhichKeyboard(specialNormalKeyboard,WIFIPassWord[i]):
                if checkExistPicture('连接网络密码输入画面',['返回按钮.png']):
                    pass
                else:
                    clickPicture('连接网络密码输入画面',['123按钮.png'])
                if checkExistPicture('连接网络密码输入画面',['常用按钮_选中.png']):
                    pass
                else:
                    clickPicture('连接网络密码输入画面',['常用按钮_非选中.png'])
                picName = wordTransToImageName(WIFIPassWord[i])
                clickPicture('连接网络密码输入画面',[picName + '.png'])
            elif belongToWhichKeyboard(specialChineseKeyboard,WIFIPassWord[i]):
                if checkExistPicture('连接网络密码输入画面',['返回按钮.png']):
                    pass
                else:
                    clickPicture('连接网络密码输入画面',['123按钮.png'])
                if checkExistPicture('连接网络密码输入画面',['中文按钮_选中.png']):
                    print('is 中文keyboard')
                else:
                    clickPicture('连接网络密码输入画面',['中文按钮_非选中.png'])
                clickPicture('连接网络密码输入画面',['中文' + WIFIPassWord[i] + '.png'])
            elif WIFIPassWord[i] == ' ':
                touch([950, 670])

        #连接
        clickPicture('连接网络密码输入画面',['连接按钮.png'])

    sleep(30)
    if checkExistPicture('连接网络密码输入画面', ['keyboard返回按钮.png'],timeout=4) :
        clickPicture('连接网络密码输入画面', ['keyboard返回按钮.png'],timeout=4)
    flick([872, 203], DIR_DOWN, step=1, speed=SPEED_NORMAL)
    flick([872, 203], DIR_DOWN, step=1, speed=SPEED_NORMAL)

assertWIFIConnected()

#确认是否有异常
checkException()
