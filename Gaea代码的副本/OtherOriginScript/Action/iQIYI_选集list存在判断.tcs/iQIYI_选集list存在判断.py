from autost.api import *

#如果存在选集list则继续，不存在则结束整个Case

if poco(text='选集').exists():
    pass
else:
    end()