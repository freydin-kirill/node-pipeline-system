from abc import abstractmethod, ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nodes import BaseNode

class BaseObserver(ABC):
    @abstractmethod
    def update(self, node: 'BaseNode'):
        raise NotImplementedError


class LoggerObserver(BaseObserver):
    def update(self, node: 'BaseNode'):
        print(f'Logger: Node {node.name} changed status to \"{node.status.value}\"')


class CascadeObserver(BaseObserver):
    def update(self, node: 'BaseNode'):
        for child in node.children:
            child.status = node.status

