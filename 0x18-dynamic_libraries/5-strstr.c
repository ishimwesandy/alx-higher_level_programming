#include "main.h"
/**
 * _strstr - Entry point
 * @haystacks: input
 * @needl: input
 * Return: Always 0 (Success)
 */
char *_strstr(char *haystacks, char *needl)
{
	for (; *haystacks != '\0'; haystacks++)
	{
		char *k = haystacks;
		char *p = needl;

		while (*k == *p && *p != '\0')
		{
			k++;
			p++;
		}

		if (*p == '\0')
			return (haystacks);
	}

	return (0);
}
