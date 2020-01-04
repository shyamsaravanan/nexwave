<%@page import="java.sql.*"%>
<%@ page import="db.DBConnection"%>
<%@ include file="header.jsp"%>

<div class="jumbotron jumbotron-fluid">
	<div class="container">
		<h1 class="display-4 ml-4">Welcome</h1>
		<a class="btn btn-primary ml-4" href="addPost.jsp">Add New Post</a>
		<a class="btn btn-danger ml-4" href="index.jsp">Logout</a>
	</div>
</div>

<div class="container">
	<%
		try {
			Connection con = DBConnection.getConnection();
			String query = "SELECT * FROM blog_articles";
			PreparedStatement pst = con.prepareStatement(query);

			ResultSet rs = pst.executeQuery();
			while (rs.next()) {
	%>

	<div class="card bg-light m-4">
		<img class="card-img-top" src="<%=rs.getString("image")%>">
		<div class="card-body">
			<h5 class="card-title"><%=rs.getString("title")%><br>
			</h5>
			<p class="card-text"><%=rs.getString("summary")%>
			</p>
		</div>
	</div>

	<%
		}
		} catch (Exception e) {
			e.printStackTrace();
		}
	%>

</div>

<%@ include file="footer.jsp"%>