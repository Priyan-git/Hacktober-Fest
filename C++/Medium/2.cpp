#include <iostream>
using namespace std;
int main()
{
    int num;
    int sum = 0;
    int digit;
    cout << "Enter an integer: ";
    cin >> num;
    while (num != 0)
    {
        digit = num % 10;
        sum = digit + sum;
        num = num / 10;
    }
    cout << "Sum of digits is: " << sum << endl;
    return 1;
}
