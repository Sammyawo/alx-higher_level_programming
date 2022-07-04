#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: single list
 * Return: 1 if it is a palin or 0 if not
 */

int is_palindrome(listint_t **head)
{
	int num = 0, p[4500], pal = 1, d = 0;
	listint_t *copyh = *head;

	if (!*head || !((*head)->next))
		return (1);

	for (d = 0; copyh; d++, copyh = copyh->next)
		p[d] = copyh->n;

	for (num = d, d = 0; d < num; d++)
	{
		if (p[d] != p[num - 1 - d])
		{
			pal = 0;
			break;
		}
	}
	return (pal);

}
