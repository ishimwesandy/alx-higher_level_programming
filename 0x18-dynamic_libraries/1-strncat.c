#include "main.h"
/**
 * _strncat - function that concatenate two strings
 * using at most num bytes from start
 * @end: input value
 * @start: input value
 * @num: input value
 *
 * Return: end
 */
char *_strncat(char *end, char *start, int num)
{
	int i;
	int j;

	i = 0;
	while (end[i] != '\0')
	{
		i++;
	}
	j = 0;
	while (j < num && start[j] != '\0')
	{
	end[i] = start[j];
	i++;
	j++;
	}
	end[i] = '\0';
	return (end);
}
