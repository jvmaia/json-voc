from org.json import JSONObject
import PythonJavaJSON

# TESTS FOR FUNCTION LOADS()

# SIMPLE JSON TEST
obj = "{'a':6, 'b':10, 'c':'teste', 'd':'iasudfnjskd', 'e':null}"
obj_json = PythonJavaJSON.loads(obj)
print(type(obj_json))
print(obj_json, end='\n\n')


# SIMPLE JSON ARRAY TEST
array = """[{'a':5, 'b':10, 'c':'test', 'd':'bbbbbbbb', 'e':null},
            {'a':5, 'b':10, 'c':'test', 'd':'cccccc'},
            {'a':5, 'b':10, 'c':'test'}]
        """
array_json = PythonJavaJSON.loads(array)
print(type(array_json))
print('ARRAY 00 --> ', array_json, end='\n\n')

# NESTED JSON ARRAY TEST 02
array01 = """[{"h": null}, {"j":2345}, [{"k":9.0}]]"""
array01_json = PythonJavaJSON.loads(array01)
print(type(array01_json))
print('ARRAY 01 --> ', array01_json, end='\n\n')


# EVERYTHING NESTED JSON OBJECT/ARRAY  TEST
nested = """
        [{"test": [{"t": 0, "e": 1}, [{"s":2}, {"t": 3}]]},
        {"test2": {"s": 2, "t": true, "f": false } }]
        """
nested_json = PythonJavaJSON.loads(nested)
print(type(nested_json))
print('NESTED --> ', nested_json, end='\n\n')
