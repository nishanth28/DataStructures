#Folding method = 8624522395 = 86+24+52+23+95
#mid-square = 44^2 = 1234 = 23%(tablesize)

#open-addressing = collision resolution-open adressing in which it tries to find the next open addresss slot for value to be stored in hash table
#linear-probing
#rehashing
#quadratic probing -> instead of constant skip-> use h+1,h+4,h+9

#chaining allows many items to be in the same slot.


class HashTable(object):

    def __init__(self,size): # initialize hash table, with 2 arrays

        self.size =  size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):     # put piece of data to correct key.

        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None: # hash is empty
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))  # next slot

                while self.slots[nextslot] != None and self.slots[nextslot]!= key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None: # new key
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    self.data[nextslot] = data # else old value

    def get(self,key):

        startslot = self.hashfuntion(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def hashfuntion(self,key,size):

        return key%size

    def rehash(self,oldhash,size):

        return (oldhash+1)%size



if __name__ ==  "__main__":

    # main function for hash!
