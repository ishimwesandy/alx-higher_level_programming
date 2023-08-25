#include "main.h"
/**
 * _strchr - fuction Entry point
 * @str: input
 * @ca: input
 * Return: Always 0 (Success)
 */
char *_strchr(char *str, char ca)
{
	int i = 0;

	for (; str[i] >= '\0'; i++)
	{
		if (str[i] == ca)
			return (&str[i]);
	}
	return (0);
}
