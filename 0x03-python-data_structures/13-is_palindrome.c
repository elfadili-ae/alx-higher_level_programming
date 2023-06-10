#include "lists.h"


/**
 * list_len - number of elements in a linked list
 * @h: linked list
 * Return: number of elements in @h
 */
int list_len(const listint_t *h)
{
	int nodes = 0;

	while (h != NULL)
	{
		h = h->next;
		nodes++;
	}
	return (nodes);
}

/**
 * getListVal - store list values in an array
 * @head: linked list
 * @vals: int array
 */
void getListVal(listint_t *head, int vals[])
{
	int i = 0;

	while (head)
	{
		vals[i] = head->n;
		i++;
		head = head->next;
	}
}
/**
 * is_palindrome - check if the list is a palindrome
 * @head: linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = list_len(*head);
	int vals[len], i;

	getListVal(*head, vals);
	if (*head == NULL)
		return (1);

	for (i = 0; i < (len / 2); i++)
	{
		if ((*head)->n != vals[len - 1 - i])
			return (0);
		*head = (*head)->next;
	}
	return (1);
}
