// Euler10.cpp : Ce fichier contient la fonction 'main'. L'exécution du programme commence et se termine à cet endroit.
//

#include "pch.h"
#include <iostream>
#include <boost/math/special_functions/prime.hpp>

bool IsPrime(int n)
{
	if (n == 1)
		return false;
	else if (n == 0)
		return false;
	else if (n == 2)
		return true;
	else if (n % 2 == 0)
		return false;
	else
	{
		int i = int(pow(n, 0.5));
		while (i > 1)
		{
			if (n%i == 0)
				return false;
			i -= 1;
		}
		return true;
	}
}
int main()
{
	uint64_t sum = 0;
	int i = 0;
	int n = 10;
	for (int i = 2 ; i <= 2000000; i++)
	{
		if (IsPrime(i))
		{
			sum += i;
		}
	}
    std::cout << "Voici la somme de tous les nombres premiers " << sum; 
}
