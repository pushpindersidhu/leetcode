from typing import Optional, Self


class Node:

    def __init__(
        self,
        key: int,
        value: int,
        prev: Optional[Self] = None,
        next: Optional[Self] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, Node] = {}

        self.least_recent = Node(0, 0)
        self.most_recent = Node(0, 0)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = Node(key, value)
        self.map[key] = node
        self.insert(node)

        if len(self.map) > self.capacity:
            assert self.least_recent.next
            least_recent_node = self.least_recent.next
            self.remove(least_recent_node)
            del self.map[least_recent_node.key]

    def insert(self, node: Node) -> None:
        assert self.most_recent.prev
        node.prev, node.next = self.most_recent.prev, self.most_recent
        node.prev.next = self.most_recent.prev = node

    def remove(self, node: Node):
        assert node.prev and node.next
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
