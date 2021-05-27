# Função que carrega dicionarios de dados "userdict" em uma lista "user_list"
def load_users():
    user_list = []
    user_dict = {
        "name": "Clark Kent", 
        "username" : "kent",
        "password" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"
    }
    user_list.append(user_dict)
    user_dict = {
        "name": "Bruce Wayne",
        "username" : "wayne",
        "password" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"
    }
    user_list.append(user_dict)
    user_dict = {
        "name": "Christopher Walker",
        "username" : "walker",
        "password" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"
    }
    user_list.append(user_dict)
    return user_list