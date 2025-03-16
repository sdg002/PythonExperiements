you were here

https://docs.python.org/3/library/configparser.html


'''
parser = configparser.ConfigParser()
parser.read_dict({'section1': {'key1': 'value1',
                               'key2': 'value2',
                               'key3': 'value3'},
                  'section2': {'keyA': 'valueA',
                               'keyB': 'valueB',
                               'keyC': 'valueC'},
                  'section3': {'foo': 'x',
                               'bar': 'y',
                               'baz': 'z'}
})
parser.sections()

[option for option in parser['section3']]
'''