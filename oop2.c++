#include<iostream>
using namespace std;
class shop
{
    int itempid[100];
    int itemprice[100];
    int counter;
    public :
     void intCounter(void)
     {
        counter=0;
     }
     void getprice(void);
     void setprice(void);
     void displayprice(void);


};
void shop:: displayprice(void){
    for (int i=0;i<counter;i++)
{
    
    cout<<"enter id"<<endl<<itemid[i]<<"is"<<itemprice[i];
}
}
int main(){

    Shop dukaan ;
    dukaan.setprice
}