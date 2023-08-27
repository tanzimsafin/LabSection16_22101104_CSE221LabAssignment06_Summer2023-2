#include<iostream>
using namespace std;
 class A{
    public:
    int arr[10];
    int sum;
    float avrg;
    void calculation(){
        for(int i=0;i<10;i++){
            cout<<"enter the element of array:";
            cin>>arr[i];
        }
    }
 };
 class B:public A{
    public:
    void summation(){
        calculation();
        sum=0;
        for(int i=0;i<10;i++){
            sum=sum+arr[i];
        }
        cout<<"sum:"<<sum<<endl;
    }
 };
 class C:public A{
    public:
    void average(){
        calculation();
        sum=0;
        for(int i=0;i<10;i++){
            sum=sum+arr[i];
        }
        avrg=(float)sum/10;
        cout<<"avrg:"<<avrg<<endl;
    }
 };
 class D:public B,public C{
 };           
int main(){
    D obj1;
    obj1.summation();
    obj1.average();
    
    return 0;
}
