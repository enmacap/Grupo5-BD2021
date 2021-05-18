package bdcontrolador;
import java.sql.*;
public class Conexion {
    private String nombreBD = "bdfuncionarios";
    private String url = "jdbc:mysql://127.0.0.1/"+nombreBD;
    private String usuario="root";
    private String pass="";
    private Connection con;
    public Conexion(){
        try{
            Class.forName("org.gjt.mm.mysql.Driver");
            con=DriverManager.getConnection(url,usuario,pass);
        }catch(ClassNotFoundException | SQLException e){
            System.out.println("Error al conectar a la base de datos");
        }
    }
    public Connection conectar(){
        return con;   
    }
} 
