#include<iostream>
using namespace std;
int main()
{
	long long int s,t,a,b,pp,ora;
	long long int m[1000],n[1000];
	cin>>s>>t>>a>>b>>pp>>ora;
	for(int i=0;i<pp;i++)
	{
		cin>>m[i];
	} 
	for(int j=0;j<ora;j++)
	{
		cin>>n[j];
	}
    int counta=0,countb=0;
	for(int i=0;i<pp;i++)
	{
		if(((a+m[i])>=s) && ((a+m[i])<=t))
			counta++;

	}
	for(int j=0;j<ora;j++)
	{
		if(((b+n[j])>=s) && ((b+n[j])<=t))
			countb++;
	}
	cout<<counta<<endl;
	cout<<countb<<endl;
}