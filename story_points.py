#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: kukulkan-Diego Fernando Galaviz

"""

import sys 

def storyPoints(tmin,tmax,prior,risk,exper):
    """
    

    Parameters
    ----------
    tmin : TYPE:float betweet (0,15])
        DESCRIPTION.ideal time estimation in days
    tmax : TYPE:float betweet (0,15])
        DESCRIPTION. whorse case time estimation
    prior : TYPE:str
        DESCRIPTION. piority of task
    risk : TYPE:str
        DESCRIPTION. risk of the task
    exper : TYPE:str
        DESCRIPTION. user experience 

    Returns
    -------
    Story point. TYPE int.

    """
    mean_t=(tmin+tmax)*0.5
    prior =prior.lower()
    risk=risk.lower()
    exper=exper.lower()
    if (mean_t <= 15 and mean_t>0 and tmin*tmax !=0):
        if (prior =='alto' or prior =='medio' or prior == 'bajo'):
            if prior =='alto':
                p=1
            if prior == 'medio':
                p=0.8
            else:
                p=1           
            
        else:
            print(f'Los parametros aceptados son bajo,medio,alto \n Y tu ingresaste {prior!r}')
            
        if (risk =='alto' or risk =='medio' or risk == 'bajo'):
            if risk =='alto':
                r=1.3
            if risk == 'medio':
                r=1
            else:
                r=0.7           
            
        else:
            print(f'Los parametros aceptados son bajo,medio,alto \n Y tu ingresaste {risk!r}')
            
        if (exper =='muy alta' or exper =='alta' or exper == 'media' or exper == 'baja'):
            if exper =='muy alta':
                ex=1
            if exper == 'baja':
                ex=0.7
            if exper == 'media':
                ex = 0.5
            
            else:
                r=0.3           
            
            step1=p*(mean_t)**r
            step2=step1/ex
            sp_raw=round(step2,2)
            if sp_raw<=1.5:
                sp = 1
            elif sp_raw<=2.5:
                sp=2
            elif sp_raw<=3.5:
                sp=3
            elif sp_raw <=6.5:
                sp=5
            elif sp_raw <=10.5:
                sp=8
            elif sp_raw <=17:
                sp=13
            elif sp_raw <=27:
                sp=21
            else:
                sp=34
            print(f'Para los siguientes parametros: \n Riesgo {risk!r}-{r!r} \n Prioridad {prior!r}-{p!r} \n Experiencia {exper!r}-{ex!r} \n Tiempo promedio {mean_t!r}: Dias' )
            print("\n \tSP_RAW:",sp_raw)
            print("\n \tSP Fibonacci:",sp)
        else:
            print(f'Los parametros aceptados son baja,media,alta y muy alta \n Y tu ingresaste {exper!r}')
        
    else:
        print(f'Los valores permitidos para t en dias deben estar en el rango:(0-15] \n Y tus valores ingresados son los siguientes: {tmin!r},{tmax!r}')
    
    return(int(sp))
            

"""    
program_name = sys.argv[0]
tiem_min = sys.argv[1]
tiem_max = sys.argv[2]
prioridad =  sys.argv[3]
riesgo =  sys.argv[4]
experiencia = sys.argv[5]
SPOINT=storyPoints(tiem_min,tiem_max,prioridad,riesgo,experiencia)
"""

if __name__ == '__main__':
   
    SPOINT=storyPoints(7,15,"Medio","bajo","media")

