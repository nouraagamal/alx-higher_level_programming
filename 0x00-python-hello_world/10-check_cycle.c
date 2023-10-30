#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function to check if a list is cycle or not
 * list: pointer
 * Return: 1 or 0 ow
*/

int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (f == s)
			return (1);
	}
	return (0);
}
