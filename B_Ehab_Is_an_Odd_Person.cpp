#include <iostream>
#include <algorithm>
using namespace std;
bool ex[2];
int arr[100005];
int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        ex[arr[i] % 2] = 1;
    }
    if (ex[0] && ex[1])
        sort(arr, arr + n);
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
}