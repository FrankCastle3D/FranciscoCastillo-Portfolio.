"""
This tools allows you to find the names of all the windows and buttons on the UE5 interface.
Then you could define a menu as follows -> menus = unreal.ToolMenus.get()
And then assign a specific menu to a variable -> main_menu = menus.find_menu("LevelEditor.MainMenu")

Then you could expand such menu with the following command:
custom_menu = main_menu.add_sub_menu("Custom Menu", "Custom Menu Entry", "Menu Name", "Menu Label")

"""
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

