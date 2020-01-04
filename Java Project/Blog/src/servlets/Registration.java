package servlets;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import db.DBConnection;

/**
 * Servlet implementation class Registration
 */
@WebServlet("/Registration")
public class Registration extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public Registration() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String username = request.getParameter("login");
		String password = request.getParameter("password");

		boolean isFilled = !(username.isEmpty() || password.isEmpty());

		if (isFilled) {
			try {
				Connection con = DBConnection.getConnection();
				String query = "INSERT INTO blog_users VALUES(?,?)";
				PreparedStatement pst = con.prepareStatement(query);

				pst.setString(1, username);
				pst.setString(2, password);

				pst.executeUpdate();

				System.out.println("Successfully inserted");
				response.sendRedirect("displayPost.jsp");
			} catch (Exception e) {
				e.printStackTrace();
			}
		} else {
			response.sendRedirect("displayError.jsp");
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
