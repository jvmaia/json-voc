from org.json import JSONObject, JSONArray
import PythonJavaJSON

# TESTS FOR FUNCTION DUMPS()

# JSON OBJECT TEST

o = {
    'a': {'b': 5},
    'd': {'e': 10},
    'f': 30,
    'g': True,
    'h': None
}
o_dump = PythonJavaJSON.dumps(o)
print(type(o_dump))
print(o_dump, end='\n\n\n')


# JSON ARRAY TEST

a = [
        {
            'a': [{'b':5, 'c':False}],
            'd': {'e': True, 'f':None},
            'g': [
                {'h': [{'i':99, 'j':'test'}]},
                {'k': 9.7}
                ]
        },
        [
            {'a0': 0},
            {
                'b0': [
                {'c0': 329485},
                {'d0': None}
                ]
            }
        ]
    ]
a_dump = PythonJavaJSON.dumps(a)
print(type(a_dump))
print(a_dump)

