from config2.config import config

#
#Cannot install this component, see the following github
#https://github.com/grimen/python-config2/issues/15
#

config.get_env() # => None
config.get() # => {'a1': 'DEFAULT 1', 'a2': {'b1': [1, 2, 3], 'b2': ['foo', 'bar'], 'b3': {'c1': 1, 'c2': 'DEFAULT 2'}}}

config.a1 # => 'DEFAULT 1'
config.a2 # => {'b1': [1, 2, 3], 'b2': ['foo', 'bar'], 'b3': {'c1': 1, 'c2': 'DEFAULT 2'}}
config.a2.b3.c2 # => 'DEFAULT 2'

print('$$$')