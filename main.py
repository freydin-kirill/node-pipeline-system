from nodes import Node
from node_status import NodeStatus
from observers import LoggerObserver, CascadeObserver


if __name__ == '__main__':
    root = Node("root")
    child1 = Node("child1")
    child2 = Node("child2")

    root.add_child(child1)
    root.add_child(child2)

    logger = LoggerObserver()
    cascade = CascadeObserver()

    root.add_subscriber(logger)
    root.add_subscriber(cascade)

    child1.add_subscriber(logger)
    child2.add_subscriber(logger)

    root.status = NodeStatus.Running