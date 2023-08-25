#include "main.h"
/**
 * _strncpy - copy a string
 * @end: input value
 * @start: input value
 * @num: input value
 *
 * Return: end
 */
char *_strncpy(char *end, char *start, int num)
{
	int j;

	j = 0;
	while (j < num && start[j] != '\0')
	{
		end[j] = start[j];
		j++;
	}
	while (j < num)
	{
		end[j] = '\0';
		j++;
	}

	return (end);
}
