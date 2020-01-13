<html>
<head>
<title>Welcome to Log Report</title>
</head>
<body>
<h1>LOG REPORT</h1>
<table border='1' bgcolor='green'>
%for ip,dt,im,url in res:
%if im=='No image':
<tr bgcolor='yellow'>
<td>{{ip}}</td>
<td>{{dt}}</td>
<td bgcolor='red'>{{im}}</td>
<td>{{url}}</td>
</tr>
%else:
<tr>
<td>{{ip}}</td>
<td>{{dt}}</td>
<td>{{im}}</td>
<td>{{url}}</td>
</tr>
%end
%end
</table>
</body>
</html>