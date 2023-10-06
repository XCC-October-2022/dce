from typing import Protocol
from dataclasses import dataclass

@dataclass
class GCPConfig():
    ...

@dataclass
class AzureConfig():
    ...


class Provider(Protocol):   
    def create_project(self):
        ...
    def delete_project(self):
        ...



