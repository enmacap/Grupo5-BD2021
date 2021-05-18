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

public class FuncionarioDAO {
    private Conexion c = new Conexion();
    private Connection con;
    // ps contiene las instrucciones sql que le pasare al servidor
    private PreparedStatement ps;
    private ResultSet rs;
    
    // Constructor
    public FuncionarioDAO() {}
    
    // Operaciones
    //Listar
    public List<Funcionario> listar() {
        ArrayList<Funcionario> lista = new ArrayList<>();
        String sql= "SELECT * FROM funcionario";
        try{
            con = c.conectar();
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()) {
                Funcionario a = new Funcionario();
                a.setId_funcionario(rs.getInt("id_funcionario"));
                a.setUsuario(rs.getString("usuario"));
                a.setPasswrd(rs.getString("passwrd"));
                a.setNombre(rs.getString("nombre"));
                a.setApellido(rs.getString("apellido"));
                a.setCorreo(rs.getString("correo"));
                a.setDepartamento_id(rs.getInt("departamento_id"));
                a.setRfid_codigo(rs.getInt("rfid_codigo"));
                lista.add(a);
            }
        }catch(Exception e) {
            
        }
        return lista;
    }
    
    // Insertar
    // insertar un nuevo registro
    public boolean insertar(Funcionario a) {
        boolean r = false;
        String sql= "INSERT INTO funcionario (id_funcionario,usuario,passwrd,"
                + "nombre,apellido,correo,departamento_id,rfid_codigo) " +
                "VALUES (?,?,?,?,?,?,?,?)";
        try {
            con = c.conectar();
            ps = con.prepareStatement(sql);
            ps.setInt(1, a.getId_funcionario());
            ps.setString(2, a.getUsuario());
            ps.setString(3, a.getPasswrd());
            ps.setString(4, a.getNombre());
            ps.setString(5, a.getApellido());
            ps.setString(6, a.getCorreo());
            ps.setInt(7, a.getDepartamento_id());
            ps.setInt(8, a.getRfid_codigo());
            int resultado = ps.executeUpdate();
            if (resultado == 0) {
                r = true;
            }
        }catch(Exception e) {
        
        }
        return r;
    }
    
    // Editar por id_funcionario
    public boolean editar(Funcionario a) {
        boolean r = false;
        String sql= "UPDATE funcionario set usuario=?, passwrd=?, nombre=?, "
                + "apellido=?, correo=?, departamento_id=?,rfid_codigo=?"
                + " WHERE id_funcionario=?";
        try {
            con = c.conectar();
            ps = con.prepareStatement(sql);
            ps.setString(1, a.getUsuario());
            ps.setString(2, a.getPasswrd());
            ps.setString(3, a.getNombre());
            ps.setString(4, a.getApellido());
            ps.setString(5, a.getCorreo());
            ps.setInt(6, a.getDepartamento_id());
            ps.setInt(7, a.getRfid_codigo());
            ps.setInt(8, a.getId_funcionario());
            int resultado = ps.executeUpdate();
            if (resultado == 0) {
                r = true;
            }
        }catch(Exception e) {
        
        }
        return r;
    }
    
    // Eliminar
        public boolean borrar(String id_funcionario) {
        String sql= "DELETE FROM funcionario WHERE id_funcionario=" + id_funcionario;
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
