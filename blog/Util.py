def deal_json_invaild(data):
    data = data.replace("\n", "\\n").replace("\r", "\\r").replace("\n\r", "\\n\\r") \
        .replace("\r\n", "\\r\\n") \
        .replace("\t", "\\t")
    data = data.replace('": "', '&&testPassword&&')\
        .replace('", "', "$$testPassword$$")\
        .replace('{"', "@@testPassword@@")\
        .replace('"}', "**testPassword**")
    print(data)

    data = data.replace('"', r'\"')\
        .replace('&&testPassword&&', '": "').replace('$$testPassword$$', '", "').replace('@@testPassword@@', '{"').replace('**testPassword**', '"}')
    print(data)
    return data