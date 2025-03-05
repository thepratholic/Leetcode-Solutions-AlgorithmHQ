// Contributed by Pratham Chelaramani (Student)
// LinkedIn: https://www.linkedin.com/in/thepratholic/


class Solution
{
public:
    long long coloredCells(int n)
    {
        long long res = n;
        return 1 + (res - 1) * res * 2; // dervied formula, nothing else
    }
};