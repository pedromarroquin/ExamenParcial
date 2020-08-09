/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package simulador.de.procesos.y.memoria;

import Funciones.Generar_Procesos;
import Funciones.Ordenar_Procesos_FCFS;
import Tipos_de_Ejecución.First_Come_First_Served;
import java.util.Collections;

/**
 *
 * @author leoma
 */
public class SimuladorDeProcesosYMemoria {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int a=5;
        Generar_Procesos genera= new Generar_Procesos(a);
        genera.Crear_Procesos();
        First_Come_First_Served FCFS = new First_Come_First_Served(genera.Lista_Procesos);
    }
}
