<%@ include file="header.jsp"%>

<div class="container">
	<h1 class="mt-4 mb-4">Add Post</h1>
	<form class="ml-4" action="Article">
		<div class="form-group">
			<label>Image</label> <input class="form-control" type="text"
				name="image">
		</div>
		<div class="form-group">
			<label>Title</label> <input class="form-control" type="text"
				name="title">
		</div>
		<div class="form-group">
			<label>Summary</label> <input class="form-control" type="text"
				name="summary">
		</div>
		<input type="submit" class="btn btn-primary" value="Add Post">
	</form>
</div>

<%@ include file="footer.jsp"%>