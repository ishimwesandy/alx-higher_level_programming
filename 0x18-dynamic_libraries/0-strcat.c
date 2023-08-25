#include "main.h"
/**
 * _strcat - function that concatenates two strings
 * @end: input value
 * @start: input value
 *
 * Return: void
 */
char *_strcat(char *end, char *start)
{
	int i;
	int j;

	i = 0;
	while (end[i] != '\0')
	{
		i++;
	}
	j = 0;
	while (start[j] != '\0')
	{
		end[i] = start[j];
		i++;
		j++;
	}

	end[i] = '\0';
	return (end);
}
