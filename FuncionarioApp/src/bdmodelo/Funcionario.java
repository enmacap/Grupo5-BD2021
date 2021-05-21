// Habilita los cambios a la Base de Datos
// DAO : Direct Access Object
// Enlace entre java y la BD
package bdmodelo;

public class Funcionario {
    // Atributos
    private int id_funcionario;
    private String usuario;
    private String passwrd;
    private String nombre;
    private String apellido;
    private String correo;
    private int departamento_id;
    private String rfid_codigo;
    
    //Constructor
    public Funcionario() {}
    
    //Set & Get
    // ID
    public int getId_funcionario() {
        return id_funcionario;
    }
    public void setId_funcionario(int id) {
        id_funcionario = id;
    }
    //  USER
    public String getUsuario() {
        return usuario;
    }
    public void setUsuario(String user) {
        usuario = user;
    }
    // PASSWORD
    public String getPasswrd() {
        return passwrd;
    }
    public void setPasswrd(String p) {
        passwrd = p;
    }
    // NAME
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String p) {
        nombre = p;
    }
    // LASTNAME
    public String getApellido() {
        return apellido;
    }
    public void setApellido(String p) {
        apellido = p;
    }
    // MAIL
    public String getCorreo() {
        return correo;
    }
    public void setCorreo(String p) {
        correo = p;
    }
    // DEPARMENT
    public int getDepartamento_id() {
        return departamento_id;
    }
    public void setDepartamento_id(int departamento_id) {
        this.departamento_id = departamento_id;
    }
    // RFID
    public String getRfid_codigo() {
        return rfid_codigo;
    }
    public void setRfid_codigo(String rfid_codigo) {
        this.rfid_codigo = rfid_codigo;
    }
}
