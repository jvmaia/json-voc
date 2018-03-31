from org.json import JSONObject
import PythonJavaJSON

obj = "{'a':5, 'b':10, 'c':'teste', 'd':'iasudfnjskd', 'e':null}"
obj_json = PythonJavaJSON.loads(obj)
print(type(obj_json))
print(obj_json, end='\n\n')

array = """[{'a':5, 'b':10, 'c':'teste', 'd':'bbbbbbbb', 'e':null},
            {'a':5, 'b':10, 'c':'teste', 'd':'cccccc', 'e':null},
            {'a':5, 'b':10, 'c':'teste', 'd':'eeeee', 'e':null }]"""
array_json = PythonJavaJSON.loads(array)
print(type(array_json))
print(array_json, end='\n\n')
