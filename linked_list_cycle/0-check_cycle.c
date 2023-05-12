#include "lists.h"

int check_cycle(listint_t *list)
{
    if (list == NULL)
    {
        return 0;
    }

    listint_t* slow = list;
    listint_t* fast = list->next;

    while (slow != fast)
    {
        if (fast == NULL || fast->next == NULL)
        {
            return 0;
        }
    slow = slow->next;
    fast = fast->next->next;
    }
    return 1;
}