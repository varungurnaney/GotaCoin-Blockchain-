import hashlib as hasher
import datetime as date


class Dabba:

#Creating Block Structure 
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
	
#Defining the hash of the block 
  def hashOfDabba(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash))
    return sha.hexdigest()
	
	def firstDabba():
		Dabba(0, date.datetime.now(), "Security is all about context", "0") 
  
#Creating not-first blocks
	def nextDabba(prevBlock,data)
		this_index = prevBlock.index + 1
		this_timestamp = date.datetime.now()
		this_data = data
		this_hash = prevBlock.hash
		return Dabba(this_index, this_timestamp, this_data, this_hash)
	
		


#Creating a blockchain of 10 Blocks


blockchain = [firstDabba()]

for i in range(0,9)

	block_to_add = nextDabba(prevBlock,"Context")
	blockchain.append(block_to_add)
	previous_block = block_to_add
	
	print "Block #{} has been added to the blockchain!".format(block_to_add.index)
	print "Hash: {}\n".format(block_to_add.hash) 

		
		
		