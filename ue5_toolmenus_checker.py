import unreal

def list_menu(num=1000):
    menu_list = set()
    for i in range (num):
        obj = unreal.find_object(None, f"/Engine/Transient.ToolMenus_0:RegisteredMenu{i}")    
        if not obj:
            continue

        menu_name = str(obj.menu_name)

        if menu_name == "None":
            continue
        
        menu_list.add(menu_name)
    return list(menu_list)

print(list_menu())