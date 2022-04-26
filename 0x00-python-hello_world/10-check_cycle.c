#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks the existennce of loops in a list
 * @list:  receives the head of a listint_t type list
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

