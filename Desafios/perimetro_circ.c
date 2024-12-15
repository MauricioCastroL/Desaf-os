// Autor: Mauricio Castro
// Fecha: 13/12/2024
// Objetivo: Calcular el perimetro de una Circunferencia

#include <stdio.h>
#define Pi 3.1416

int main(){
    float radio, circ;

    printf("Ingrese el valor del radio: ");
    scanf("%f", &radio);
    
    if(radio > 0){
        circ = 2 * radio * Pi;
        printf("El valor del radio es: %f", circ);
    }
    else{
        printf("No se puede calcular si el radio es negativo");
    }

}

