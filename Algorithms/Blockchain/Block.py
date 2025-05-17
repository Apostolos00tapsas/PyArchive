"""
Script Name: Block.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Class that implments one block.

"""
class Block:
    def __init__(self,out_id,out_hash,out_next_hash,out_prev_hash):
        self.id=out_id
        self.hash=out_hash
        self.next_hash=out_next_hash
        self.prev_hash=out_prev_hash

    def __repr__(self):
        return "id:{0},\n hash:{1},\n next_hash:{2},\n prev_hash:{3}\n".format(self.id,self.hash,self.next_hash,self.prev_hash)


