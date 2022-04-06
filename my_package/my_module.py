# %%

import os

# %%

def list_content(folder):
    """
    Parameters
    ----------
    folder : string
        Relative or absolute path to folder.

    Returns
    -------
    None.

    """
    files = os.listdir(folder)
    print(f"You have the following content in {folder}:")
    for file in files:
        print(file)