#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - frees a listint_t list
 *
 * @list: pointer for checking if the list has a cycle
 * Return: 1 if list has a cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *top = list;
	listint_t *nare = list;

	while (top != NULL)
	{
		top = top->next;
		nare = nare->next;

		if (nare == NULL || nare->next == NULL)
			break;
		nare = nare->next;
		if (top == nare)
			return (1);
	}
	return (0);
}
