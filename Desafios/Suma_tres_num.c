// Autor: Mauricio Castro
// Fecha: 13/12/2024
// Objetivo: Suma de tres números

#include <stdio.h>

int main(){
    int x , y, z, suma;

    printf("Ingrese el valor para x: ");
    scanf("%i", &x);

    printf("Ingrese el valor para y: ");
    scanf("%i", &y);

    printf("Ingrese el valor para z: ");
    scanf("%i", &z);

    suma = x + y + z;

    printf("La suma de x,y y z es: %i", suma);

}