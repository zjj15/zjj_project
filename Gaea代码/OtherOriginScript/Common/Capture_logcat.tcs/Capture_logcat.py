from autost.api import *

logtag = "su\
\n logcat -G 200M\
\n setprop persist.iauto.log.switch 31\
\n setprop persist.log.tag V\
\n setprop persist.log.tag.appupdate true\
\n setprop persist.log.tag S\
\n setprop persist.log.tag.UI-SETTING-COM V\
\n setprop persist.log.tag.APP-SETTINGFC-MODEL V\
\n setprop persist.log.tag.IVI-MMGR-AVTMGR V\
\n setprop persist.log.tag.IVI-HUCOM-SI V\
\n setprop persist.log.tag.IVI-HUCOM-SC V\
\n setprop persist.log.tag.IVI-HUCOM-NU V\
\n setprop persist.log.tag.IVI-DATAMGR-SVC V\
\n setprop persist.log.tag.IVI-DATAMGR-G V\
\n setprop persist.log.tag.IVI-DATAMGR-PROXY V\
\n setprop persist.log.tag.IVI-DATAMGR-IMPL V"

logcat = 'adb logcat -s UI-SETTING-COM APP-SETTINGFC-MODEL IVI-MMGR-AVTMGR IVI-HUCOM-SI IVI-HUCOM-SC IVI-HUCOM-NU IVI-DATAMGR-SVC IVI-DATAMGR-G IVI-DATAMGR-PROXY IVI-DATAMGR-IMPL |grep -vE "92 40|5a 02 12|12 40|sendMiconDtlogDataAck|NHuCom|TransmitFrame|5a 02 f1|5a 02 31|ChangeTx|30 40|5a 02 14"' 
start_capturing_log(shell_cmd = "logcat -s UI-SETTING-COM APP-SETTINGFC-MODEL IVI-MMGR-AVTMGR IVI-HUCOM-SI IVI-HUCOM-SC IVI-HUCOM-NU IVI-DATAMGR-SVC IVI-DATAMGR-G IVI-DATAMGR-PROXY IVI-DATAMGR-IMPL |grep -vE "92 40|5a 02 12|12 40|sendMiconDtlogDataAck|NHuCom|TransmitFrame|5a 02 f1|5a 02 31|ChangeTx|30 40|5a 02 14"")