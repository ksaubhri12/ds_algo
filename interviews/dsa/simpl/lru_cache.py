# 1 2 3
# 2 3 4
# 2 4 3
# 4 3 2
# 3 2 5

class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.prev = None
        self.next = None


class LRU_CACHE:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.end = None
        self.value_map = {}
        self.current_capacity = 0

    def put(self, key: str, value_string: str):
        if key in self.value_map:
            return self.put_if_key_exists(key, value_string)

        if self.current_capacity < self.capacity:
            end_node = Node(value_string, key)
            if self.head is None:
                self.head = end_node
                self.value_map[key] = end_node
                self.current_capacity = self.current_capacity + 1
                self.end = self.head

            else:
                curr_end_node = self.end
                self.end = end_node
                curr_end_node.next = end_node
                end_node.prev = curr_end_node
                self.value_map[key] = end_node
                self.current_capacity = self.current_capacity + 1

        else:
            curr_key = self.head.key
            del self.value_map[curr_key]
            new_node = Node(value_string, key)
            curr_head = self.head
            self.head = curr_head.next
            del curr_head
            curr_end = self.end
            self.end = new_node
            curr_end.next = new_node
            new_node.prev = curr_end

    def put_if_key_exists(self, key: str, value_str: str):
        value_node = self.value_map[key]
        pre_value_node = value_node.prev
        next_value_node = value_node.next
        pre_value_node.next = next_value_node
        next_value_node.prev = pre_value_node
        new_node = Node(value_str, key)
        self.value_map[key] = new_node
        curr_end = self.end
        self.end = new_node
        curr_end.next = new_node
        new_node.prev = curr_end

    def get(self, key: str):
        if key not in self.value_map:
            return "-1"

        value_node = self.value_map[key]
        pre_value_node = value_node.prev
        next_value_node = value_node.next
        pre_value_node.next = next_value_node
        next_value_node.prev = pre_value_node
        curr_end = self.end
        self.end = value_node
        curr_end.next = value_node
        value_node.prev = curr_end
        value_node.next = None
        return value_node.data

    def print_lru_cache(self):
        curr = self.head
        while curr is not None:
            print(curr.data, curr.key, end='')
            print()
            curr = curr.next


if __name__ == '__main__':
    lru_cache = LRU_CACHE(3)
    print('Add Kalpesh')
    lru_cache.put("kalpesh", "saubhri")
    lru_cache.print_lru_cache()
    print()
    print('Add Vikram')
    lru_cache.put("vikram", "chauhan")
    lru_cache.print_lru_cache()
    print()
    print('Add Sai')
    lru_cache.put("sai", "reddy")
    lru_cache.print_lru_cache()
    print()

    print('Get Vikram')
    lru_cache.get("vikram")
    lru_cache.print_lru_cache()
    print()
    print('Add Sai rama')
    lru_cache.put("sai", "rama")
    lru_cache.print_lru_cache()
