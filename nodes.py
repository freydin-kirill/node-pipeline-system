from abc import ABC
from typing import List, Optional

from node_status import NodeStatus
from observers import IObserver


class INode(ABC):
    def add_subscriber(self, subscriber: IObserver):
        pass

    def remove_subscriber(self, subscriber: IObserver):
        pass

    def notify_subscribers(self):
        pass


class BaseNode(INode):
    def __init__(self, name: str,
                 status: Optional[NodeStatus] = None,
                 children: Optional[List[INode]] = None):
        self._name = name
        self._status = status if status is not None else NodeStatus.Pending
        self._children = children if children is not None else []
        self._subscribers: List[IObserver] = []

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
    def children(self) -> List[INode]:
        return self._children

    @children.setter
    def children(self, children: INode):
        self._children = children

    @property
    def subscribers(self) -> List[IObserver]:
        return self._subscribers

    def add_subscriber(self, subscriber: IObserver):
        self._subscribers.append(subscriber)
        for child in self._children:
            child: BaseNode
            if subscriber not in child.subscribers:
                child.add_subscriber(subscriber)

    def remove_subscriber(self, subscriber: IObserver):
        self._subscribers.remove(subscriber)
        for child in self._children:
            child.remove_subscriber(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)


class Node(BaseNode):
    pass
