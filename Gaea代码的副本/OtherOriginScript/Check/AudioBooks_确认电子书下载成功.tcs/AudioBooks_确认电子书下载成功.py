from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if not exists(Template("../../Design/Audiobook_download_delete_icon.png")):
    print('该书没有下载功能')
    pass
else:
    assert_exists(Template('../../Design/Audiobook_download_delete_icon.png'),timeout=60)
    