#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,number;
	char c;
	string str1,str2;
	cin>>n;
	map<string,int> friends;
	for(int i=0;i<n;i++)
	{
		getline(cin,str1);
		cin>>number;
		friends[str1]=number;
	}
	while(getline(cin,str2) && !friends.empty()){
		if(friends.count(str2)>0)
			cout<<str2<<"="<<friends[str2]<<endl;
		else
			cout<<"Not found"<<endl;
	}
}