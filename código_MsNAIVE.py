# df a imputar
df_new = df.copy()

# df con valores sin na y filtro
df_var = df.filter(regex = 'ing|cost' , axis = 1)
# o
#Señalar todas las variables que no necesitar ser imputadas.
var_nd = ['fraude', 'muestra']
#Variables a imputar
var_x = [x for x in df_new.columns if x not in var_nd]

for i in df_var.columns.tolist(): #ó poner for i in var_x:
    
    umbral_unique = 10 # Scalar
    umbral_nan = 0.1 # Scalar
    target = 'fraude' # Columna df.
    muestra = 'muestra' # Columna df.
    ventana = 'Train' # Atributo de la Columna Muestra.
    
    #Criterio 1: Umbral de Missing Value
    porc_i = round(df[i].isnull().sum()/len(df[i]),4)
    
    #Criterio 2: Cantidad de Valores Unicos
    unique_val = df[i].loc[df[muestra]==ventana].nunique()
    
    # Imputación por Regresión variables continuas y categorias de caracter continuas.
    if porc_i <= umbral_nan and unique_val >= umbral_unique:
        
        print('La variable '+i ,'fue imputada con MEDIANA DE CLASE', 'con',+unique_val,'valores únicos y',porc_i, 'valores perdidos.' )        
        
        for j in df[target].unique():
            
            # Calculo de mediana de la variable(i) en función de la clase target(j).
            median_xclass = df[i].loc[(df[target]== j) & (df[muestra]==ventana)].median()
            # Reemplaza los NaN a las variable(i) en función de la clase target(j).
            df_new[i].loc[(df[i].isna()) & (df[target]== j)] = median_xclass
                        
    # Elimina variables con MISSING VALUE mayor al Umbral y un único valor en los valores únicos.                                            
    elif porc_i > umbral_nan or unique_val <= 1:
        
        print('La variable '+i ,'fue ELIMINADA por tener',porc_i, 'valores perdidos.' )  
        
        df_new.drop(i, axis = 1, inplace = True)
        
        
    # Imputación por CATEGORIA FALTANTE a varaibles dicotomicas y variables con menos de 15 categorias.
    elif unique_val > 1  & unique_val < umbral_unique:
        
        print('La variable '+i ,'fue imputada por VALOR FALTANTE', 'con',+unique_val,'valores únicos y',porc_i, 'valores perdidos.' )        
        
        #Calculo máximo valor
        value_max = df[i].max()
        #Valor máximo +1
        value_mas1 = value_max + 1
        #Reemplazar NaN por el Valor asignado.
        df_new[i].fillna(value_mas1, inplace = True)
#FIN
