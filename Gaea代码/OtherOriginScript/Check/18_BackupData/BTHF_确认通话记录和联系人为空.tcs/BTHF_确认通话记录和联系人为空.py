from autost.api import *

try:
    assert_exists(Template('../../../Design/BT_Contact_Records_empty.png'))
except:
    error('Contact Records empty Check Error!')