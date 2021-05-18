// Habilita los cambios a la Base de Datos
// DAO : Direct Access Object
// Enlace entre java y la BD
package bdmodelo;
// Librerias
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import bdcontrolador.Conexion;

public class TarjetaDAO {
    private Conexion c = new Conexion();
    private Connection con;
    // ps contiene las instrucciones sql que le pasare al servidor
    private PreparedStatement ps;
    private ResultSet rs;
    
    // Constructor
    public TarjetaDAO() {}
    
    // Operaciones
    //Listar
    public List<Tarjeta> listar() {
        ArrayList<Tarjeta> lista = new ArrayList<>();
        String sql= "SELECT * FROM tarjeta";
        try{
            con = c.conectar();
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()) {
                Tarjeta a = new Tarjeta();
                a.setCodigo_rfid(rs.getInt("codigo_rfid"));
                lista.add(a);
            }
        }catch(Exception e) {
            
        }
        return lista;
    }
    
    // Insertar
    // insertar un nuevo registro
    public boolean insertar(Tarjeta a) {
        boolean r = false;
        String sql= "INSERT INTO funcionario (codigo_rfid) " +
                "VALUES (?)";
        try {
            con = c.conectar();
            ps = con.prepareStatement(sql);
            ps.setInt(1, a.getCodigo_rfid());
            int resultado = ps.executeUpdate();
            if (resultado == 0) {
                r = true;
            }
        }catch(Exception e) {
        
        }
        return r;
    }
    
    // Editar por id_departamento
    public boolean editar(Tarjeta a) {
        boolean r = false;
        String sql= "UPDATE funcionario codigo_rfid=?";
        try {
            con = c.conectar();
            ps = con.prepareStatement(sql);
            ps.setInt(1, a.getCodigo_rfid());
            int resultado = ps.executeUpdate();
            if (resultado == 0) {
                r = true;
            }
        }catch(Exception e) {
        
        }
        return r;
    }
    
    // Eliminar
    public boolean borrar(String codigo_rfid) {
        String sql= "DELETE FROM tarjeta WHERE codigo_rfid=" + codigo_rfid;
        try {
            con = c.conectar();
            ps = con.prepareStatement(sql);
            int resultado = ps.executeUpdate();
            if (resultado == 0)
                return true;
        }catch(Exception e) {
        
        }
        return false;
    }
}