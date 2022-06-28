#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a new node at sort of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *top = *head, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	for (; top != NULL; top = top->next)
	{
		if (number <= top->n)
		{
			*head = new;
			new->next = top;
			return (new);
		}
		if (number >= top->n && top->next == NULL)
		{
			new->next = NULL;
			top->next = new;
			return (new);
		}
		if (number >= top->n && number <= top->next->n)
		{
			new->next = top->next;
			top->next = new;
			return (new);
		}
	}
	return (NULL);

}
