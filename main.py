from nodes import BaseNode as Node
from node_status import NodeStatus
from observers import LoggerObserver, CascadeObserver


if __name__ == '__main__':
    logger = LoggerObserver()
    cascade = CascadeObserver()

    root = Node("root")
    child1 = Node("child1")
    child2 = Node("child2")
    child3 = Node("child3", NodeStatus.Running)

    root.children = [child1, child2, child3]
    root.add_subscriber(logger)
    root.add_subscriber(cascade)

    root.status = NodeStatus.Running
    root.status = NodeStatus.Failed
