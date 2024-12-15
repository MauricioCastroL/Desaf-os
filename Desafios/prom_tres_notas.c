//Autor: Mauricio Castro
//Fecha: 13/12/2024
//Objeticvo: Calcular promedio de tres notas

#include <stdio.h>


int main(void)
{
    int cali_1;
    int cali_2;
    int cali_3;

    printf("Se le pedira ingresar tres calificaciones para poder calcular su promedio. \n");

    printf("Ingrese su primera calificación: ");
    scanf("%i", &cali_1);

    printf("Ingrese su segunda calificación: ");
    scanf("%i", &cali_2);

    printf("Ingrese su tercera calificación: ");
    scanf("%i", &cali_3);

    float promedio = ((cali_1 + cali_2 + cali_3) / 3);

    if(promedio >=40){
        printf("Haz pasado\n");
    }
    else{
        printf("No haz pasado\n");
    }

    printf("Su promedio de notas es de %f",promedio);

}