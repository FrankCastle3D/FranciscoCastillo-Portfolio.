'''

This tool prints to console all the components inside of a bp.

TOOD:
1) Polish the data and dump it on a csv.
2) Separate the metadata injection code into a different script.
3) Make the tool a bit more robust. -> Will get more ideas in the future hopefully xD

'''


import unreal

selected_class = [unreal.Blueprint,
                  unreal.Material,
                  unreal.PackedLevelActor]
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets_of_class(selected_class[0])
sub_object_data_subsystem = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
sub_object_data_library = unreal.SubobjectDataBlueprintFunctionLibrary
def list_of_tags(selection):
    # This function lists the tags on selected actors.
    for asset in selection:
        asset_class = asset.get_class()
        default_object = asset.get_default_object()
        asset_outer = asset.get_outer()
        asset_default_object = asset.get_default_object()
        set_tags = unreal.EditorAssetLibrary.set_metadata_tag(asset,"HasName",f"{asset.get_name()}")
        asset_tags = unreal.EditorAssetLibrary.get_metadata_tag(asset,"HasName")
        print(asset_tags)
def list_of_sub_objects(selection):
    # This class will make a list of all the components inside of a blueprint.
    for asset in selection:
        asset_class = asset.get_class()
        bp_data = sub_object_data_subsystem.k2_gather_subobject_data_for_blueprint(asset)
        for data in bp_data:
            sub_object_data = sub_object_data_library.get_data(data)
            owner_name = sub_object_data_library.get_display_name(sub_object_data)
            components = sub_object_data_library.get_variable_name(sub_object_data)

            print(owner_name)
            #print(">>> " + str(components))

#list_of_sub_objects(selected_assets)
