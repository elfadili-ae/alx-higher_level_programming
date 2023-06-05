#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a linked list
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = (list->next)->next;

	while (fast && slow && slow->next && slow->next->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = (fast->next)->next;
	}

	return (0);
}
