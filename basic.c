#include<stdio.h>
void main(){
    /*printf("Hello World");

    char ar[50];
    printf("Enter name: "); // Prompt first
    scanf("%s", ar);      // Read input (no & for strings)
    printf("Hello, %s", ar);
    return 0; // Explicit return
    int num1,num2;
    num1=15;
    num2=7;
    printf("%d %d %d %d %d",num1+num2,num1-num2,num1*num2,num1/num2,num1%num2);*/
    int age;
    printf("Enter age: "); // Prompt first
    scanf("%d",&age); 
    if (age>18){
        printf("You are an adult");
    }
    else{
        printf("You're a minor");
    }
}