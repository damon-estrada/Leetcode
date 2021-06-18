/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode * prev, * curr, * next;
    prev = NULL;
    curr = head;
    
    if (curr != NULL)
        next = head -> next;
    
    while (curr != NULL) {
        curr -> next = prev;
        prev = curr;
        curr = next;
        if (next) // kinda hack, but whatevah
            next = curr -> next;
    }
    return prev;
}