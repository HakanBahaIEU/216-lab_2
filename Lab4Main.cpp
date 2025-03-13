#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }
    void push(int x) {
        if(num < 0){
            head->data = x;
        } else {
            Node *Temp = nullptr;
            Temp->data = x;
            if(num<capacity){
                Temp->next = head;
                head = Temp;  
            } else {
                increaseCapacity();
                cout<<"Capacity increased!";
                Temp->next = head;
                head = Temp;
            } 
        }

        
    }

    int pop() {
        int r = head->data;
        cout<<r<<" is going to be popped!";
        Node *Temp;
        Temp = head;
        head = head->next;
        delete Temp;
        return r;
    }
    int peek() {
        cout<<"Head data is:"<<head->data;
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity = capacity*2;
    }

    bool deleteElement(int val) {
        bool found = false;
        Node *Temp;
        Node *PreviousTemp;
        Temp = head->next;
        PreviousTemp = head;

        if(head->data == val){
            head = head->next; 
            delete Temp;
        }

        while(found == false && Temp->next != nullptr){
            if(Temp->data == val){
                PreviousTemp->next = Temp->next;
                delete Temp;
                found = true;
            }
            Temp = Temp->next;
            PreviousTemp = PreviousTemp->next;
        }
    }
};

int main() {

    return 0;
}
