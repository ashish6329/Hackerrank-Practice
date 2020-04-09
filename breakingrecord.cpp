#include<iostream>
#include <bits/stdc++.h> 
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
	int res=arr[0];
	int rss=arr[0];
	int count=0,countb=0;
	for(int i=1;i<n;i++)
	{
		if(arr[i]<res)
		{
			res=min(res,arr[i]);
			count++;
		}
		if(arr[i]>rss)
		{
			rss=max(res,arr[i]);
			countb++;
		}
	}
	cout<<countb<<" "<<count;

}