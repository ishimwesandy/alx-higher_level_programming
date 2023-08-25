#include "main.h"
/**
 * _memset - fill  the blocks of memory with a specific values
 * @start: starting address of memory to be filled
 * @d: the desired value
 * @num: number of bytes to be changed
 *
 * Return: changed array with new value for n bytes
 */
char *_memset(char *start, char d, unsigned int num)
{
	int i = 0;

	for (; num > 0; i++)
	{
		start[i] = d;
		num--;
	}
	return (start);
}
