from tkinter import filedialog
from path_getter.path_getter_interface import PathGetterInterface


class PathGetter(PathGetterInterface):

    def get_file_path(self) -> str:
        return filedialog.askopenfilename(
            title="Select Image",
            filetypes=[('image files', '.jpg')])

