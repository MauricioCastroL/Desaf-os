// Autor: Mauricio Castro
// Fecha: 13/12/2024
// Objetivo: Comparar dos números

#include <stdio.h>

int main(){
    int x, y;

    printf("Ingrese el valor del primer número: ");
    scanf("%i", &x);

    printf("Ingrese el valor del segundo número: ");
    scanf("%i", &y);

    if(x > y){
        printf("El primer número es mayor");
    }
    else if(x < y){
        printf("El segundoo número es mayor");
    }
    else{
        printf("Ambos son iguales");
    }

}