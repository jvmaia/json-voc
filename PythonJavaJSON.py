from org.json import JSONObject, JSONArray


def getKeysObject(jsonObject):
    keys = []
    keysIterator = jsonObject.keySet().iterator()
    while keysIterator.hasNext():
        keys.append(keysIterator.next())

    return keys


def getKeysArray(jsonArray):
    length = jsonArray.length()
    keys = [i for i in range(length)]
    return keys


def jsonToDict(json):
    keys = getKeysObject(json)
    json_dict = {}
    for key in keys:
        if json.isNull(key):
            value = None
        else:
            value = json.get(key)
        json_dict[key] = value

    return json_dict


def loads(s):
    if s.startswith('{'):
        objJson = JSONObject(s)
        python_json = jsonToDict(objJson)
        return python_json
    else:
        json = JSONArray(s)
        keys = getKeysArray(json)
        python_json = []

    for key in keys:
        objJson = json.get(key)
        objDict = jsonToDict(objJson)
        python_json.append(objDict)

    return python_json
