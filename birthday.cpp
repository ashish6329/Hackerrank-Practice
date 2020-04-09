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
	int d,m;
	cin>>d>>m;
	int count=0;
	for(int i=0;i<n-1;i++)
	{
		int sum=0;
		for(int j=0;j<m;j++)
		{
			sum=sum+arr[i+j];
		}
		if(d==sum)
			count++;
		
	}
	cout<<count;
}
