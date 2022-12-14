# [[PYTHON] Naive Treatment of Missing Value (MsNAIVE)](https://drive.google.com/drive/folders/1DdL8TVdPWpVj0AarBVqaYjVkgfcQTSFv?usp=sharing)

- #### Creado, por: Franco A. Mansilla Ibañez, Chile.
- website: https://www.francomansilla.com


`versión 1.0- 09/2022`

## Descripción: 

1. Este código permite hacer missing value en función a la variable target dicotomica o categorica, si es que tu proposito es realizar un modelo con forma supervisada. 
2. Utiliza los valores para clacular mediana de la variable x en funcion a la clase target (y) para imputar los NaN de las variables x.


## Instalación:
Nota 1: Es código que se puede utilizar en la misma interfaz usuario. 
Nota 2: Descargar [BBDD](https://github.com/fmansillaib/python_MsNAIVE/blob/main/BD%20MsNAIVE.xlsx) y [.ipynb](https://github.com/fmansillaib/python_MsNAIVE/blob/main/MsNAIVE.ipynb) para ver los [ejemplos](https://drive.google.com/drive/folders/1DdL8TVdPWpVj0AarBVqaYjVkgfcQTSFv?usp=sharing). 
 

## Syntax 

En Python copiar el código, señalar:

- [ ] **umbral_unique**: Señalar el umbral de valores unicos para considerarlo como categorica o categorica de caracter continuo.
- [ ] **umbral_nan**: Señalar el umbral de missing value para considerarlo en la imputación.
- [ ] **variable_y**: Señalar la variable target para aplicar la imputación. **OJO:** target discreto o categorico.
- [ ] **variable_x**: Señalar la(s) variable(s) para imputar.
- [ ] **muestra**: Señalar la muestra en la que se define muestras **TRAIN** y **TEST**.
- [ ] **ventana**: Señalar la ventana la cual se considera para hacer los calculos, tal como: **TRAIN** o **TEST**.


