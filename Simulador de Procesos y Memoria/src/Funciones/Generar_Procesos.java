/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Funciones;
import Clases.Proceso;
import java.util.ArrayList;

/**
 *
 * @author leoma
 */
public class Generar_Procesos {
    public int n;
    public int m=100;
    public ArrayList<Proceso>Lista_Procesos;
    
    public Generar_Procesos(int n){
        this.Lista_Procesos = new ArrayList<Proceso>();
        this.n=n;
    }
    
    public Generar_Procesos(ArrayList<Proceso>Lista_Procesos){
        this.Lista_Procesos=Lista_Procesos;
    }
    
    public void Crear_Procesos(){
        for (int i=0;i<n;i++){
          Lista_Procesos.add(new Proceso(m));
          m++;
        }
    }
    public void Imprimir_Procesos(){
          for (int i=0;i<n;i++){
          Lista_Procesos.get(i).Imprimir_Proceso();
        }
    }

    
    public int getN() {
        return n;
    }

    public void setN(int n) {
        this.n = n;
    }
    
      
}
