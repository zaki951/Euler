#include <iostream>

bool isDivisible(int n)
{
    for (int i = 1 ; i<= 20 ; i++)
        if (n%i != 0) 
            return false;
    return true;
}

int main()
{
    int i = 20;
    while(1)
    {
        if (isDivisible(i))
            break;
        i+= 1;
        
    }
    std::cout << "Voici le résultat : " <<  i;
    return i;
}