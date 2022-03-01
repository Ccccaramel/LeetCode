#include <iostream>
#include <vector>
#include <string.h>
#include <stdio.h>
using namespace std;
class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        return "null";
    }
};
int main()
{
    // char arr[][]=["flower","flow","flight"];
    char s[] = "Golden Global      View,disk * desk";
    const char *d = " ,*";
    char *p;
    p = strtok(s, d);
    cout << "p:" << p << endl;
    while (p)
    {
        printf("%s\n", p);
        p = strtok(NULL, d);
        cout << "(p):" << p << endl;
    }
    return 0;
}