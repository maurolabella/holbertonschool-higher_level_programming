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
	int array[1024], i = 0, j = 0;
	listint_t *current;

	if (!(*head) || !((*head)->next->next))
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

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}