#include "main.h"
/**
 * _strpbrk - Entry point
 * @str: input
 * @acc: input
 * Return: Always 0 (Success)
 */
char *_strpbrk(char *str, char *acc)
{
		int j;

		while (*str)
		{
			for (j = 0; acc[j]; j++)
			{
			if (*str == acc[j])
			return (str);
			}
		str++;
		}

	return ('\0');
}
