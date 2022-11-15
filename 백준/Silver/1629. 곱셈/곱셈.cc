#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll a,b,c;
ll mod(ll n,ll k,ll r){
	if(k==1){
		return n%r;
	}
	ll ret=mod(n,k/2,r);
    ret=(ret*ret)%r;
	if(k%2){
        return (n*ret)%r;
    }
	return ret;	
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin>>a>>b>>c;
	
	cout<<mod(a,b,c)<<'\n';			
	return 0;
}