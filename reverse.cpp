#include<iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	int temp,j;
	for(int i=0;i<n;i++)
	{
		j=n-1;
		temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
		j--;
		cout<<arr[j]<<" ";
	}

}