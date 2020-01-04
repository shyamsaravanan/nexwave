package db;

import java.sql.*;

public class DBConnection {
	public static Connection getConnection() {
		String DB_URL = "jdbc:oracle:thin:@localhost:1521:orcl";
		String USER = "scott";
		String PASS = "tiger";

		Connection con = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			con = DriverManager.getConnection(DB_URL, USER, PASS);
			System.out.println("Connected to database");
			return con;
		} catch (Exception e) {
			System.out.println("Could not connect to database");
			e.printStackTrace();
		}
		return null;
	}
}