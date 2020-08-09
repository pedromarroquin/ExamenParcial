/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Tipos_de_Ejecución;
import Clases.Proceso;
import Funciones.Generar_Procesos;
import Funciones.Ordenar_Procesos_FCFS;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.Collections;
import javax.swing.JTextField;
/**
 *
 * @author leoma
 */
public class First_Come_First_Served {
    ArrayList<Proceso>Lista_Procesos;
    int n;
    
    public First_Come_First_Served(ArrayList<Proceso>Lista_Procesos){
        Collections.sort(Lista_Procesos,new Ordenar_Procesos_FCFS());
        this.Lista_Procesos=Lista_Procesos;
        n=0;
    }
    
    public void Ejecucion_FCFS(){
        KeyListener escuchaTeclado=new KeyListener() {
            @Override
            public void keyTyped(KeyEvent ke) {  
            }
            @Override
            public void keyPressed(KeyEvent ke) {
                n=Lista_Procesos.get(0).getBurst_Time();
                n=n-1;
                if(n==0){
                    Lista_Procesos.remove(0);
                }else{
                    Lista_Procesos.get(0).setBurst_Time(n);
                }
                Generar_Procesos imprimir = new Generar_Procesos(Lista_Procesos);
                imprimir.Imprimir_Procesos();
            }

            @Override
            public void keyReleased(KeyEvent ke) {
            }   
        };
        while(Lista_Procesos.size()>0){
            KeyEvent ke = null;
            escuchaTeclado.keyPressed(ke);
        }
        
    }
}
