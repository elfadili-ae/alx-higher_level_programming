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
void getListVal(listint_t *head, int *vals, int len)
{
	int i = 0, j = 0;

	while (j < len)
	{
		if (j > (len / 2) - 1)
		{
			vals[i] = head->n;
			i++;
		}
		j++;
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
	int *vals, len, i, isOdd = 0;
	listint_t *tmp = *head;

	if (tmp == NULL || tmp->next == NULL)
		return (1);

	len = list_len(tmp);
	if (len % 2 == 0)
		isOdd = 1;
	if (len == 2 && tmp->n == tmp->next->n)
		return (1);
	else if (len == 2 && tmp->n != tmp->next->n)
		return (0);

	vals = malloc(sizeof(int) * (len / 2));
	if (vals == NULL)
		exit(1);

	getListVal(tmp, vals, len);
	for (i = 0; i < (len / 2); i++)
	{
		if ((tmp)->n != vals[(len / 2) - isOdd - i])
		{
			free(vals);
			return (0);
		}
		tmp = (tmp)->next;
	}
	free(vals);
	return (1);
}
