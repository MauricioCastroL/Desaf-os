// Autor: Mauricio Castro
// Fecha: 13/12/2024
// Objetivo: Calculadora básica (+,-,*,/)

#include <stdio.h>

int main(){
    char operacion;
    float x, y;
    float r;
    
    printf("Ingrese la operación que desea: ");
    scanf("%s", &operacion);

    printf("Ingrese el valor para x: ");
    scanf("%f", &x);

    printf("Ingrese el valor para y: ");
    scanf("%f", &y);


    if(operacion == '+'){
        r = x + y;
        printf("la suma es: %f", r);
    }
    else if(operacion == '-'){
        r = x - y;
        printf("la resta es: %f", r);
    }
    else if(operacion == '*'){
        r = x * y;
        printf("la multiplicación es: %f", r);
    }
    else if (operacion == '/')
    {
        if (y == 0 || (y == 0 && x == 0)){
            printf("No se puede dividir por cero o 0/0 no es definido");
        }
        else{
            r = x / y;
            printf("la división es: %f", r);
        }
    }
    

}