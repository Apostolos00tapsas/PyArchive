from Block import *
import hashlib as hl
import uuid
import xml.etree.ElementTree as ET
import numpy as np

"""
Script Name: Blockchain.py
Author: Apostolos Tapsas
Copyright: © 2024 Apostolos Tapsas (https://github.com/Apostolos00tapsas)

Description:
    Implements a block chain.

Parameters:
    
    
Returns:
    ybc: Blockchain
    n:   Blocks
    

Example:
    ybc,n=createblock()
"""

def createblock():
    blockchain=[]
    blocks=0
    answer=input("Do you wand to input or delete number in queue ? y=insert/n=delete: ")
    while answer =='y' or answer=='n':
        id = uuid.uuid4()
        if len(blockchain)==0 and answer=='n':
            print ("The Blockchain is empty")
            answer=input("Do you wand to input or delete number in queue ? y=insert/n=delete: ")
        elif len(blockchain)!=0 and answer=='n':
            print ("You can not delete any block")
            answer=input("Do you wand to input or delete number in queue ? y=insert/n=delete: ")
        else:
            if blocks==0:
                blockchain.append(Block(id.hex,hl.sha256(str(id.hex)).hexdigest(),-1,-1))
                blocks+=1
                answer=input("Do you wand to input or delete number in queue ? y=insert/n=delete: ")
            else:
                blockchain[-1].next_hash=hl.sha256(str(id.hex)).hexdigest()
                blockchain.append(Block(id.hex,hl.sha256(str(id.hex)).hexdigest(),-1,blockchain[-1].hash))
                blocks+=1
                answer=input("Do you wand to input or delete number in queue ? y=insert/n=delete: ")

    return blockchain,blocks

def save_blockchain(bck,n):
    tree = ET.ElementTree()
    blockchain = ET.Element("Blockchain")
    for i in range(0,n):
        node =  ET.Element(str('Node')+str(i+1),node_id = str(bck[i].id), node_hash = str(bck[i].hash), next_hash=str(bck[i].next_hash) ,previous_hash= str(bck[i].prev_hash))
        blockchain.append(node)
    tree._setroot(blockchain)
    tree.write("bc.xml")
    


def from_xml(xml_name):
    xml_tree = ET.parse(xml_name)
    root = xml_tree.getroot()
    blockchain=[]
    for i in range(0,len(root)):
        blockchain.append(Block(root[i].attrib['node_id'],root[i].attrib['node_hash'],root[i].attrib['next_hash'],root[i].attrib['previous_hash']))
    return blockchain
    
    

ybc,n=createblock()
#save_blockchain(bc,n)
#x = from_xml("bc.xml")




