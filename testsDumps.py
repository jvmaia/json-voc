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
print(o_dump)
