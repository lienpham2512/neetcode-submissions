class ListNode{
    public:
        int value;
        ListNode* next;
        ListNode(int value): value(value), next(nullptr) {}
        ListNode(int value, ListNode* next): value(value), next(next) {}
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;
public:
    LinkedList() {
        head = new ListNode(-1);
        tail = head;
    }

    int get(int index) {
        int i = 0;
        ListNode* current = head->next;
        while (current != nullptr){
            if(i==index){
                return current->value;
            }
            i++;
            current = current->next;
        }
        return -1;
    }

    void insertHead(int val) {
        ListNode* newNode = new ListNode(val, head->next);
        head->next = newNode;
        if(newNode->next == nullptr){
            tail = newNode;
        }
    }
    
    void insertTail(int val) {
        tail->next = new ListNode(val);
        tail = tail->next;
    }

    bool remove(int index) {
        int i = 0;
        ListNode* current = head;
        // move current to point to the node before the node we want to delete, manipulate using ->next
        while (i < index && current->next != nullptr){
            i++;
            current = current->next;
        }
        if(current->next != nullptr){ // this ensure that the index is not out of bound
            if(current->next == tail){
                tail = current;
            }
            ListNode* toDelete = current->next;
            current->next = current->next->next;
            delete toDelete;
            return true;
        }
        return false;
    }

    vector<int> getValues() {
        vector<int> allValues;
        ListNode* current = head->next;
        while(current != nullptr){
            allValues.push_back(current->value);
            current = current->next;
        }
        return allValues;
    }
};
