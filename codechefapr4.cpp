#include<bits/stdc++.h>
using namespace std;
int main()
{
	long int t;
	cin>>t;
	while(t--)
	{
		long int n;
		cin>>n;
		bool arr[n];
		int i;
		for(int i=0;i<n;i++)
		{
			cin>>arr[i];
		}
		int count=0;
		for(int i=0;i<n;i++)
		{ 

			
			if((arr[i]==1) && (arr[6*i]==1) || (arr[i]==1))
			{
				count++;
			}
			



			

		}
		cout<<count<<endl;
		
		if(count==1)
		{
			cout<<"YES"<<endl;

		}
		else if((count%2==0) || (n%2==1)) 
		{
			cout<<"YES"<<endl;
		}
		else 
			cout<<"NO"<<endl;



	
}
}