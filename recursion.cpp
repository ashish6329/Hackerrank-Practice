#include<iostream>
using namespace std;
long long multiple(long long a, long long b) 

{
	long long int c=10000009;

  if (b == 0) { 
      return 0 ;

  }

  long long ret = multiple(a, b >> 1)  ;

  ret = (ret + ret) % c  ;

  if (b & 1) {

      ret = (ret + a) % c  ;
  }
  return ret;
}
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		long long int x,y;
		cin>>x>>y;
		cout<<multiple(x,y)<<endl;
	}
}