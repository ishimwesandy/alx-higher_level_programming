#include "lists.h"
listint_t *reverse_listint(listint_t **h);
int is_palindrome(listint_t **h);

/**
 * reverse_listint -  function Reverses a singly-linked listint_t list.
 * @h: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **h)
{
	listint_t *node = *h, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*h = prev;
	return (*h);
}
/**
 * is_palindrome - fucntion that Checks if a singly linked list is a palindrome.
 * @h: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **h)
{
	listint_t *tmps, *rev, *md;
	size_t s = 0, i;

	if (*h == NULL || (*h)->next == NULL)
		return (1);

	tmps = *h;
	while (tmps)
	{
		s++;
		tmps = tmps->next;
	}

	tmps = *h;
	for (i = 0; i < (s / 2) - 1; i++)
		tmps = tmps->next;

	if ((s % 2) == 0 && tmps->n != tmps->next->n)
		return (0);

	tmps = tmps->next->next;
	rev = reverse_listint(&tmps);
	md = rev;

	tmps = *h;
	while (rev)
	{
		if (tmps->n != rev->n)
			return (0);
		tmps = tmps->next;
		rev = rev->next;
	}
	reverse_listint(&md);

	return (1);
}
