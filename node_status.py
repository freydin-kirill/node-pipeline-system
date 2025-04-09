from enum import Enum


class NodeStatus(Enum):
    Pending = 'pending'
    Running = 'running'
    Success = 'success'
    Failed = 'failed'
