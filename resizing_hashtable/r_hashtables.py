

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
        self.collisionsSinceResize = 0


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
        while currentNode is not None:  # Possible 0(n) operation
            if currentNode.key == key:
                # We've updated the current value of a key that matches a key already in place
                currentNode.value = value 
                # Nothing else to do here.
                return None
            currentNode = currentNode.next
        if currentNode is None:
            # We have a collision
            hash_table.collisionsSinceResize += 1
            ''' I won't actually be writing this code here, but I would check for resize during the insert normally.
            if hash_table.collisionsSinceResize > 2:
                # We've had multiple collisions since last resize
                hash_table_resize(hash_table)
            '''
            # We didn't return out so we didn't find an exisiting value to update.
            newPair = LinkedPair(key, value)
            newPair.next = hash_table.storage[index]
            hash_table.storage[index] = newPair
    # The base node hasn't been set yet.
    else:
        hash_table.storage[index] = LinkedPair(key, value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    currentNode = hash_table.storage[index]
    previousNode = hash_table.storage[index]
    if currentNode is not None:
        while currentNode is not None:
            if currentNode.key == key:
                # Check if we're at the base node
                if currentNode is hash_table.storage[index]:
                    # If this is the only node here.
                    if currentNode.next is None:
                        # Just remove this node
                        hash_table.storage[index] = None
                        return None
                    else:
                        # We have a next node
                        # Set the base node to the next node
                        hash_table.storage[index] = hash_table.storage[index].next
                        return None
                else:
                    # If currentNode isn't the base node
                    # Check if we have a next node
                    if currentNode.next is not None:
                        # currentNode is in between nodes in the list
                        # Update previousNode to point to the next node, effectively deleting currentNode
                        # This is where I would also free up memory in none garbage collected languages.
                        previousNode.next = currentNode.next
                        return None
                    else:
                        # This is the last node so we just set previousNode.next to be none
                        previousNode.next = None
                        return None
            
            # previousNode will only be the currentNode for the first run through
            previousNode = currentNode
            # Secondary + run throughs will have the previousNode be the last node we checked
            currentNode = currentNode.next
    if currentNode is None:
        print(f'There is no key: {key} in the hash table.')
        return 1
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    currentNode = hash_table.storage[index]
    if currentNode is not None:
        while currentNode is not None:
            # When we find a matching key return its value.
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next
    if currentNode is None:
        # No matching nodes found
        return None

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    # Create a new hash table because we're going to use the functions we already created.
    newHT = HashTable(hash_table.capacity * 2)
    # 0(n) We're going through and shuffling things over to the new array(list)
    for i in range(0, len(hash_table.storage)):
        currentNode = hash_table.storage[i] # If we've fallen out of the loop below, this is set at a base node not a collision.
        # This will loop until we're done with any collisioned LinkedList
        while currentNode is not None:
            hash_table_insert(newHT, currentNode.key, currentNode.value) # This inserts everything, base nodes and collisioned lists
            # We're going to check for any collisioned nodes here and reset things in the new hash table
            currentNode = currentNode.next
            
    return newHT

def Testing():
    
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")
    
    ht = hash_table_resize(ht)
    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))
    print("######################")
    hash_table_remove(ht, "line_3")
    hash_table_remove(ht, "line_2")
    hash_table_remove(ht, "line_1")
    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))
    print("#####################")
    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")
    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))
    
    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
        + " to " + str(new_capacity) + ".")
    

Testing()
