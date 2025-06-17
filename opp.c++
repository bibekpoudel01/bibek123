#include<iostream>
using namespace std;
class animal
{
   
    private:
    int age;
    string name;
    
    public :
    string color;
    int soundrange;
    int kxa;
    void setData(int age1,string name1);
    void getData(){
    cout<<"the age of animal"<<age;
    cout<<"the name of aanimeal"<<name;
    cout<<"color"<<color;
    cout<<"soundrange"<<soundrange;
    cout<<"kxa"<<kxa;
    }




   


    
};
void animal::setData(int age1, string name1){
    age=age1;
    name=name1;

}
int main()
{
    animal bibek;
    bibek.color="red";
    bibek.soundrange=12;
    bibek.kxa=123;
    bibek.setData(20,"bibekpoudel");
    bibek.getData();
    return 0;
}
