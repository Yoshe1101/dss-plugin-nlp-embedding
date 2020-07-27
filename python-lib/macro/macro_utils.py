from macro.model_configurations import MODEL_CONFIFURATIONS

def read_model_inputs(config):
    macro_inputs = {}
    macro_inputs["language"] = config.get("language",None)
    #Add mapping language ISO <--> Language readable format
    
    model_name = config.get("modelName",None)
    model_id =[x["id"] for x in MODEL_CONFIFURATIONS.values() if x["family"] == model_name][0] 
    macro_inputs["embedding_model"] = model_id

    macro_inputs["output_folder_name"] = config.get("outputFolder",None)
    macro_inputs["transformer_shortcut_name"] = config.get("transformersModelVersion",None)

    return macro_inputs

def is_folder_exist(project,output_folder_name):
    managed_folders_list = [x["name"] for x in project.list_managed_folders()]
    return True if output_folder_name in managed_folders_list else False

def manage_model_folder(output_folder_name,project_key,client):
    project = client.get_project(project_key)

    #If needed, create the managed folder
    if not is_folder_exist(output_folder_name):
        output_folder = project.create_managed_folder(output_folder_name)
    
    return output_folder