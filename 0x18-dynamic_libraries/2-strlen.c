#include "main.h"
/**
 * _strlen - returns the length of a string
 *unction that returns the length of a string.
 *
 * @s: string
 * Return: length
 */
int _strlen(char *s)
{
	int longis = 0;

	while (*s != '\0')
	{
		longis++;
		s++;
	}

	return (longis);
}

