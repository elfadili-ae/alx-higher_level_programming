#include "lists.h"

/**
 * reverse_listint - reverse a listint_t
 * @head: listint_t's head
 * Return: value of poped element
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp1, *tmp2 = NULL;

	if (*head == NULL)
		return (*head);

	if ((*head)->next != NULL)
	{
		while ((*head)->next != NULL)
		{
			tmp1 = (*head);
			(*head) = (*head)->next;
			tmp1->next = tmp2;
			tmp2 = tmp1;
		}
		(*head)->next = tmp1;
	}
	return (*head);
}

/**
 * is_palindrome - check if the list is a palindrome
 * @head: linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *fast, *slow;

	if (tmp == NULL || tmp->next == NULL)
		return (1);

	for (fast = slow = tmp; fast && fast->next;)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		fast = reverse_listint(&slow->next);
	else
		fast = reverse_listint(&slow);

	while (fast)
	{
		if (fast->n != tmp->n)
			return (0);

		tmp = (tmp)->next;
		fast = fast->next;
	}
	return (1);
}
