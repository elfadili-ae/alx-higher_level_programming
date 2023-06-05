#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a linked list
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list->next;
	fast = (list->next)->next;

	while (fast)
	{
		if (slow == fast)
		{
			slow = list;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}

			slow = slow->next;
			while (slow != fast)
			{
				slow = slow->next;
			}

			return (1);
		}

		slow = slow->next;
		fast = (fast->next)->next;
	}

	return (0);
}
