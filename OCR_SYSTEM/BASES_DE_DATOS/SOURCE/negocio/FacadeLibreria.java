package negocio;

import accesoDatos.RepositorioLibro;
import entidades.Libro;
import java.util.List;

public class FacadeLibreria {

    public List<Libro> ConsultarLibrosPorAutor(String p_author, int p_rating) {
        RepositorioLibro repo = new RepositorioLibro();
        return repo.ConsultarLibrosPorAutor(p_author, p_rating);
    }
    

    public List<Libro> ConsultarLibros() {
        RepositorioLibro repo = new RepositorioLibro();
        return repo.ConsultarLibros();
    }
}
