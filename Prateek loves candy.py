'''
Prateek recently graduated from college. To celebrate,
he went to a candy shop and bought all the candies.
The total cost was a number upto which there are n prime numbers
(starting from 2). Since Prateek wants to minimize his cost,
he calls you to help him find the minimum amount that needs
to be paid. Being a student of Prateek bhaiya it is now
your job to help him out :)

Input Format
First line contains a single integer denoting the number of test
cases T. Next T lines contains a single integer N,
denoting the number of primes required.

Constraints
T <= 10000

It is guaranteed that the answer does not exceed 10^6.

Output Format
Print the minimum cost that needs to be paid.

Sample Input
2
5
1
Sample Output
11
2
Explanation
In the first case there are 5 primes upto 11(2,3,5,7,11).
'''


def findCost(num):
    ans = []
    if num == 1:
        return 2
    if num == 2:
        return 3
    ans.append(2)
    ans.append(3)
    divisor, count, n = 2, 2, 5
    while count != num:
        if isPrime(n):
            ans.append(n)
            count += 1
        n += 1
    if len(ans) == num:
        return ans[-1]


def isPrime(n):
    divisor = 2
    while divisor < n // 2:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


if __name__ == '__main__':
    n = input("Enter number ")
    print(findCost(int(n)))
