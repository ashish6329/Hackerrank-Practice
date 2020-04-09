#include<iostream>
using namespace std;
int getmaxones(int arr[],int n)
{
	int count=0;
	int result=0;
	for(int i=0;i<n;i++)
	{
		if(arr[i]==0)
			count=0;
		else
		{
			count++;
			result=max(count,result);
		}

	}
	return result;
}
int main()
{
	int n;
	int k;
	cin>>n;
	int arr[32],i=0;
	while(n>0)
	{
		arr[i]=n%2;
		n=n/2;
		i++;


	}

	for(int j=i-1;j>=0;j--)
	{
		k=getmaxones(arr,i);

	}
	cout<<k;
}