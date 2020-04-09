#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		 int x,k,a;
	 	cin>>x>>k;
	    	
		a=x+k;
		bool prime[a+1];
		int count=0;
		for(int p=2;p*p<=a;p++)
		{
			if(prime[p]==true)
			{
				for(int i=p*p;i<=a;i++)
					prime[i]=false;
			}
		}
		for(int p=2;p<=a;p++)
		{
			if(prime[p])
				count++;
		}
		if(count==k)
			cout<<"1"<<endl;
		else
			cout<<"0"<<endl;

	}
}