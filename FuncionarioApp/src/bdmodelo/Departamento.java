package bdmodelo;
public class Departamento {
    // Atributos
    private int id_departamento;
    private String nombre;
    
    // Constructor
    public Departamento() {}
    
    // Set & Get
    // ID
    public int getId_departamento() {
        return id_departamento;
    }
    public void setId_departamento(int id) {
        id_departamento = id;
    }
    // NAME
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String n) {
        nombre = n;
    }
    
}
