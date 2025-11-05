import os

def get_cwd()->dict:
    """ This returns the current working directory.
    returns: status and cwd(current working directory)
    """
    
    try:
        cwd=os.getcwd()
        return {
            "status":"success",
            "cwd":cwd
        }
    except:
        return{
            "status":"error",
            "cwd":"Working Directory fetch issue."
        }

def mkdir(dir_location:str,dir_name:str)->dict:
    """ This function makes folder in the directory specified as argument with the specified name.
    
    Args: dir_location(str): This is the specified directory where the folder creation should be run, dir_name(str): this is the name of the folder to be created.
    
    returns: status
    """
    try:
        os.chdir(dir_location)
        os.mkdir(dir_name)
        return{
            "status":"success"
        }
    except:
        return{
            "status":"error"
        }
        

def chdir(dir_name:str)->dict:
    """change the current working directory to the specific dorectory passsed as argument
    args: dir_name(str): The directory name specified by user
    return: status
    """
    
    try:
        os.chdir(dir_name)
        return{
            "status":"success"
        }
    except:
        return{
            "status":"error"
        }
    
    
def create_file(file_name:str,content:str="")->dict:
    """This creates a file with user specified contents passed in the argument
    args: content(str): This is the user specified content to be written as file cotent, file_name(str): is the user specified file name to be created. If user don't specify any file name just don't pass any content argument.
    
    returns: status
    """
    
    try:
        with open(file_name,"w") as f:
            f.write(content)
        return{
            "status":"success"
        }
    except:
        return{
            "status":"error"
        }
# print(get_cwd())