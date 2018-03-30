from org.json import JSONObject


def getKeys(jsonObject):
    keys = []
    keysIterator = jsonObject.keySet().iterator()
    while keysIterator.hasNext():
        keys.append(keysIterator.next())

    return keys

print(getKeys(JSONObject('{"a":235, "b":null, "c":235, "z":15, "15":30}')))
