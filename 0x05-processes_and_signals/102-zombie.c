#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - function to run infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program to fork 5 child processes
 * Return: infinite_while
 */
int main(void)
{
	pid_t zombie;
	size_t n = 0;

	for (; n < 5; n++)
	{
		zombie = fork();
		if (zombie == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", zombie);
	}
	return (infinite_while());
}
