#include <map>

class Node
{
public:
  int val;
  Node *next;
  Node *random;

  Node(int _val)
  {
    val = _val;
    next = NULL;
    random = NULL;
  }
};

class Solution
{
public:
  Node *copyRandomList(Node *head)
  {
    if (!head)
    {
      return NULL;
    }
    Node *tmp = head;
    Node *tail = new Node(tmp->val);
    Node *newHead = tail;
    std::map<Node *, Node *> hashMap;
    hashMap[tmp] = tail;
    tmp = tmp->next;
    while (tmp)
    {
      tail->next = new Node(tmp->val);
      hashMap[tmp] = tail->next;
      tail = tail->next;
      tmp = tmp->next;
    }
    Node *newTail = newHead;
    Node *tmp2 = head;
    while (newTail and tmp2)
    {
      newTail->random = hashMap[tmp2->random];
      newTail = newTail->next;
      tmp2 = tmp2->next;
    }
    return newHead;
  }
};