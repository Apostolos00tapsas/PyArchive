#include <iostream>
#include <string>
using namespace std;

struct node
{
    string id;
    string hash;
    node *next;
    
    
};

class blockchain
{
private:
    node *head,*tail;
public:
    blockchain()
    {
        head = NULL;
        tail = NULL;
    }

    void add_node(string n,string k)
    {
        node *tmp = new node;
        tmp->id = n;
        tmp->hash = k;
        tmp->next = NULL;

        if(head == NULL)
        {
            head = tmp;
            tail = tmp;
        }
        else
        {
            tail->next = tmp;
            tail = tail->next;
        }
    }
    
    void display()
    {
        node *tmp;
        tmp = head;
        if (head==NULL){
        	cout<<"The Blockchain is empty"<<endl;
		}
        while (tmp != NULL)
        {
            cout << tmp->id<<"\n"<<tmp->hash<<"\n"<< endl;
            tmp = tmp->next;
        }
    }
};
