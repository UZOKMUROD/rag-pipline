import os

folder_name = ""

chats = []
def chunker():
    
    for filename in os.listdir(folder_name):
        if filename.endswith(".txt"):
            
            full_path = os.path.join(folder_name, filename)
            
            with open(full_path, "r", encoding="utf-8") as file:
                context = file.read()
                chats.append(context)        

    
    return chats
       