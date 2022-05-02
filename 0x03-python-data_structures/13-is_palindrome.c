#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check 'palindrome' status of a list
 *
 * @head: header of list received
 * Return: int 0 if not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	int array[3000], i = 0, j;
	listint_t *current;

	if (!(*head) || !((*head)->next))
		return (1);

	current = *head;

	while (current)
	{
		array[i++] = current->n;
		current = current->next;
	}
	i--;
	for (j = 0; j < i; j++, i--)
	{
		if (array[j] != array[i])
			return (0);
	}
	return (1);
}
