from autost.api import *
import os


threshold = 0.8
target_template = Template('pic/capture_20210510150304610774.png')




def get_lateset_png(path):
    log_files = [os.path.join(path, log) for log in os.listdir(path) if log.endswith(".txt") and log.startswith("log_")]
    if len(log_files):
        with open(log_files[0], "r", encoding="utf8") as f:
            file_content = f.readlines()
        if file_content[-1].find("case result: Passed(0)") != -1:
            
            return None
    filenames = [os.path.join(path, pic) for pic in os.listdir(path) if pic.endswith(".png")]
    filenames.sort()
    if len(filenames):
        return filenames[-1]
    else:
        return None
 
 
 
def walk_files(path):
    latest_png = get_lateset_png(path)
    if latest_png:
        match_confidence, _ = match_template(Template('pic/capture_20210510150304610774.png'), Template(latest_png))
        print("=======matched========", match_confidence, latest_png)
        with open("stat.txt", "a+") as f:
            f.writelines("\t".join([str(match_confidence), latest_png + "\n"]))
#        if match_confidence > threshold:
#            print("=======matched========", match_confidence, latest_png)
 
 
 
 
i = 0
path = r'D:\gitlab\morley\Test\test2.tcs\log'
print("====path=======", path)
for log_dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, log_dir)):
        walk_files(os.path.join(path, log_dir))
        i += 1
    if i > 4400:
        break
 
 
 
 
 
 
 