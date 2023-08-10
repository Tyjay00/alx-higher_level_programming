#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * 
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		return (1);
	}
	return (0);
}

