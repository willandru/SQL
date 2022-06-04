
package presentacion;

import entidades.Libro;
import java.util.List;
import negocio.FacadeLibreria;


public class PantallaLibreria {

     public static void main(String[] args){
         
        FacadeLibreria rl = new FacadeLibreria();
        List<Libro> libros = rl.ConsultarLibros();
        for (Libro lib : libros) {
            System.out.println("libro:" + lib.toString());
            System.out.println("Hola1");
        }
        libros = rl.ConsultarLibrosPorAutor("e", 1);
        for (Libro lib : libros) {
            System.out.println("libro:" + lib.toString());
            System.out.println("Hola2");
        }
    }
    
}
