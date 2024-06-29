#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    //사전순 정렬
    sort(phone_book.begin(), phone_book.end());
    
    for(int i=0; i<phone_book.size()-1; i++){
    if(phone_book[i+1].find(phone_book[i]) == 0) //인덱스 0부터 phone_book[i+1]는 index 0부터 phone_book[i]이 일치할 때.
        return false;
}
    return true;
}