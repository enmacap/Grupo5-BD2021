// Me permite conectar con la base de datos
package bdcontrolador;
import java.sql.*;
public class Conexion {
    // Atributos
    private String nombreBD = "bdfuncionarios";
    private String url = "jdbc:mysql://127.0.0.1/"+nombreBD;
    private String usuario="root";
    private String pass="";
    // Es necesario el objeto de tipo connection, de la libreria java.sql.*
    private Connection con;
    // Constructor
    public Conexion(){
        // Cargamos el driver para instanciar el objeto: con
        // Carga del driver + instanciacion: puede generar errores
        //por lo que:
        try{
            // el codigo susceptible a generar errores
            Class.forName("org.gjt.mm.mysql.Driver");
            con=DriverManager.getConnection(url,usuario,pass);
        }catch(ClassNotFoundException | SQLException e){
            System.out.println("Error al conectar a la base de datos");
        }
    }
    // Clase que me retorna el objeto que necesito para interactuar con la BD
    public Connection conectar(){
        return con;   
    }
} 
