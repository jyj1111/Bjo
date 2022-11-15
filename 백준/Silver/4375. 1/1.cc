#include <bits/stdc++.h>
using namespace std;
int n;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	while(cin>>n){
		int res=1;
		int i=1;
		while(true){
			if(res%n==0){
				
				break;
			}else{
				res=res*10+1;
				res=res%n;
				i++;
			}
		}
		
	    cout<<i<<"\n";	
						
	}
				
	return 0;
}