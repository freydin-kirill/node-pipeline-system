from abc import ABC
from typing import List, Optional

from node_status import NodeStatus
from observers import BaseObserver


class BaseNode(ABC):
    def __init__(self, name: str, status: Optional[NodeStatus] = None, children: Optional[List['BaseNode']] = None):
        self._name = name
        self._status = status if status is not None else NodeStatus.Pending
        self._children = children if children is not None else []
        self._subscribers: List[BaseObserver] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def status(self) -> NodeStatus:
        return self._status

    @status.setter
    def status(self, new_status: NodeStatus):
        if new_status != self._status:
            self._status = new_status
            self.notify_subscribers()

    @property
    def children(self) -> List['BaseNode']:
        return self._children

    @children.setter
    def children(self, children: 'BaseNode'):
        self._children = children

    def add_child(self, child: 'BaseNode'):
        self._children.append(child)

    def remove_child(self, child: 'BaseNode'):
        self._children.remove(child)

    def add_subscriber(self, subscriber: BaseObserver):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: BaseObserver):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)


class Node(BaseNode):
    pass
