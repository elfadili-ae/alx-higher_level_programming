#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - add an element to the sorted lined list
 * @head: listint_t's head
 * @n: int value
 * Return: adress of the new node | NULL (failed)
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *newNode, *tmp = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = n;
	if (tmp != NULL)
	{
		if (n <= tmp->n)
		{
			newNode->next = tmp;
			(*head) = newNode;
		}
		else
		{
			while (tmp->next != NULL)
			{
				if (n <= tmp->next->n)
					break;
				tmp = tmp->next;
			}
			if (tmp != NULL)
				newNode->next = tmp->next;
			else
				newNode->next = NULL;
			tmp->next = newNode;
		}
	}
	else
		(*head) = newNode;

	return (newNode);
}
