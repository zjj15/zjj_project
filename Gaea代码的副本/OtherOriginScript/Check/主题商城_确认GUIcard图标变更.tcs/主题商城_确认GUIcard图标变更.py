from autost.api import *

keyevent(HOME)

# confirm card icon of science theme
assert_exists(Template('../../Design/GUI_store_card_icon_science_theme.png'), threshold=0.9, timeout=5)