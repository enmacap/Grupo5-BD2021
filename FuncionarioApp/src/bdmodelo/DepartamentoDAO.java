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

public class DepartamentoDAO {
    private Conexion c = new Conexion();
    private Connection con;
    // ps contiene las instrucciones sql que le pasare al servidor
    private PreparedStatement ps;
    private ResultSet rs;
    
    // Constructor
    public DepartamentoDAO() {}
    
    // Operaciones
    //Listar
    public List<Departamento> listar() {
        ArrayList<Departamento> lista = new ArrayList<>();
        String sql= "SELECT * FROM departamento";
        try{
            con = c.conectar();
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()) {
                Departamento a = new Departamento();
                a.setId_departamento(rs.getInt("id_departamento"));
                a.setNombre(rs.getString("nombre"));
                lista.add(a);
            }
        }catch(Exception e) {
            
        }
        return lista;
    }
    
    // Insertar
    // insertar un nuevo registro
    public boolean insertar(Departamento a) {
        boolean r = false;
        String sql= "INSERT INTO funcionario (id_departamento,nombre) " +
                "VALUES (?,?)";
        try {
            con = c.conectar();
            ps = con.prepareStatement(sql);
            ps.setInt(1, a.getId_departamento());
            ps.setString(2, a.getNombre());
            int resultado = ps.executeUpdate();
            if (resultado == 0) {
                r = true;
            }
        }catch(Exception e) {
        
        }
        return r;
    }
    
    // Editar por id_departamento
    public boolean editar(Departamento a) {
        boolean r = false;
        String sql= "UPDATE funcionario set nombre=?"
                + " WHERE id_departamento=?";
        try {
            con = c.conectar();
            ps = con.prepareStatement(sql);
            ps.setString(1, a.getNombre());
            ps.setInt(2, a.getId_departamento());
            int resultado = ps.executeUpdate();
            if (resultado == 0) {
                r = true;
            }
        }catch(Exception e) {
        
        }
        return r;
    }
    
    // Eliminar
    public boolean borrar(String id_departamento) {
        String sql= "DELETE FROM departamento WHERE id_departamento=" + id_departamento;
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
