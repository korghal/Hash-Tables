

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381

    for char in string:
        hash = ((hash << 5) + hash) + ord(char)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        # Check to see if the key is already in the linked list
        currentNode = hash_table.storage[index]
        while currentNode is not None:
            if currentNode.key == key:
                # We've updated the current value of a key that matches a key already in place
                currentNode.value = value 
                # Nothing else to do here.
                return None
            currentNode = currentNode.next

        if currentNode is None:
            # We didn't return out so we didn't find an exisiting value to update.
            hash_table.storage[index] = LinkedPair(key, value).next = hash_table.storage[index]
    # The base node hasn't been set yet.
    else:
        hash_table.storage[index] = LinkedPair(key, value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")
    
    #print(hash_table_retrieve(ht, "line_1"))
    #print(hash_table_retrieve(ht, "line_2"))
    #print(hash_table_retrieve(ht, "line_3"))

    #old_capacity = len(ht.storage)
    #ht = hash_table_resize(ht)
    #new_capacity = len(ht.storage)

    #print("Resized hash table from " + str(old_capacity)
    #      + " to " + str(new_capacity) + ".")


Testing()
