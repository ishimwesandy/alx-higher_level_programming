#include "main.h"
/**
 *_memcpy - a function that copies memory areas
 *@end: memory where is stored
 *@start: memory where is copied
 *@num: number of bytes
 *
 *Return: copied memory with n bytes changed
 */
char *_memcpy(char *end, char *start, unsigned int num)
{
	int r = 0;
	int i = num;

	for (; r < i; r++)
	{
		end[r] = start[r];
		num--;
	}
	return (end);
}
