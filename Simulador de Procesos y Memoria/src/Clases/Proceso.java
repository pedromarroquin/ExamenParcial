/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;
import java.lang.Math;

/**
 *
 * @author leoma
 */
public class Proceso {
    int ID;
    String Nombre_Proceso;
    int Burst_Time;
    int Tiempo_Arribo;
    int Prioridad;
    String Estado_Proceso;
    
    public Proceso(int n,String Nombre_Proceso,int Burst_Time,int TiempoArribo){
        this.ID= n;
        this.Nombre_Proceso= Nombre_Proceso;
        this.Burst_Time= Burst_Time;
        this.Tiempo_Arribo= TiempoArribo;
        this.Estado_Proceso= "Iniciado";
        this.Prioridad=0;
    }
    public Proceso(int n){
        this.ID= n;
        this.Nombre_Proceso= "Random "+n;
        this.Burst_Time= (int) (Math.random()*10);
        this.Tiempo_Arribo= (int) (Math.random()*20);
        this.Estado_Proceso= "Iniciado";
        this.Prioridad=0;
    }
    
    public Proceso(Proceso n){
        this.ID=n.ID;
        this.Nombre_Proceso=n.Nombre_Proceso;
        this.Burst_Time=n.Burst_Time;
        this.Tiempo_Arribo=n.Tiempo_Arribo;
        this.Prioridad=n.Prioridad;
        this.Estado_Proceso=n.Estado_Proceso;
    }

    public Proceso() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    public void Imprimir_Proceso(){
        System.out.println(this.ID);
        System.out.println(this.Nombre_Proceso);
        System.out.println(this.Burst_Time);
        System.out.println(this.Tiempo_Arribo);
        System.out.println(this.Prioridad);
        System.out.println(this.Estado_Proceso);
    }
            
    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getNombre_Proceso() {
        return Nombre_Proceso;
    }

    public void setNombre_Proceso(String Nombre_Proceso) {
        this.Nombre_Proceso = Nombre_Proceso;
    }

    public int getBurst_Time() {
        return Burst_Time;
    }

    public void setBurst_Time(int Burst_Time) {
        this.Burst_Time = Burst_Time;
    }

    public int getTiempo_Arribo() {
        return Tiempo_Arribo;
    }

    public void setTiempo_Arribo(int Tiempo_Arribo) {
        this.Tiempo_Arribo = Tiempo_Arribo;
    }

    public int getPrioridad() {
        return Prioridad;
    }

    public void setPrioridad(int Prioridad) {
        this.Prioridad = Prioridad;
    }

    public String getEstado_Proceso() {
        return Estado_Proceso;
    }

    public void setEstado_Proceso(String Estado_Proceso) {
        this.Estado_Proceso = Estado_Proceso;
    }
    
}
