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
 * Servlet implementation class Article
 */
@WebServlet("/Article")
public class Article extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public Article() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		PrintWriter pw = response.getWriter();

		String image = request.getParameter("image");
		String title = request.getParameter("title");
		String summary = request.getParameter("summary");

		boolean isFilled = !(image.isEmpty() || title.isEmpty() || summary.isEmpty());

		if (isFilled) {
			try {
				Connection con = DBConnection.getConnection();
				String query = "INSERT INTO blog_articles VALUES(?,?,?)";
				PreparedStatement pst = con.prepareStatement(query);

				pst.setString(1, image);
				pst.setString(2, title);
				pst.setString(3, summary);

				pst.executeUpdate();

				System.out.println("Successfully inserted post");
				response.sendRedirect("displayPost.jsp");
			} catch (Exception e) {
				e.printStackTrace();
			}
		} else {
			System.out.println("Not filled properly");
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
