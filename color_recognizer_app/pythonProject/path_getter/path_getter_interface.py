from abc import ABC, abstractmethod


class PathGetterInterface(ABC):

    @abstractmethod
    def get_file_path(self) -> str:
        pass
