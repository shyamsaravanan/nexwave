<%@ include file="header.jsp"%>

<div class="container">
	<h1 class="mt-4 mb-4">REGISTRATION</h1>
	<form class="ml-4" action="Registration">
		<div class="form-group">
			<label>Username</label> <input class="form-control" type="text"
				name="login">
		</div>
		<div class="form-group">
			<label>Password</label> <input class="form-control" type="password"
				name="password">
		</div>
		<input type="submit" class="btn btn-primary" value="Register">
	</form>
</div>

<%@ include file="footer.jsp"%>