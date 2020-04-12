//The prime factors of 13195 are 5, 7, 13 and 29.

//What is the largest prime factor of the number 600851475143 ?

#include <math.h>
#include <iostream>

struct uint256_t
{
    std::uint64_t bits[4];
};

bool IsPrime(long unsigned n)
{
    if (n == 1)
        return false;
    else if (n == 0)
        return false;
    else if(n==2)
        return true;
    else if (n%2 == 0)
        return false;
    else 
    {
        long unsigned i = int(pow(n,0.5));
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
    auto n = static_cast<uint128>(pow(11,42));
    std::cout << n << std::endl;
    auto i = int(pow(n,0.5));
    while (i > 1)
    {
        if (n % i == 0)
            if (IsPrime(i))
                break;
        i-= 1;
    }
    std::cout << i;
    return 0;
}