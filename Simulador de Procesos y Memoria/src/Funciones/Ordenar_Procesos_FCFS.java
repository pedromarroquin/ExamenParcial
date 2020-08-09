/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Funciones;

import Clases.Proceso;
import java.util.Comparator;

/**
 *
 * @author leoma
 */
public class Ordenar_Procesos_FCFS implements Comparator<Proceso> {
    
    @Override
    public int compare(Proceso p1, Proceso p2){
        if(p1.getTiempo_Arribo()< p2.getTiempo_Arribo()){
            return -1;
        }else if(p1.getTiempo_Arribo()>p2.getTiempo_Arribo()){
            return 0;
        }else{
            return 1;
        }
    }
}
