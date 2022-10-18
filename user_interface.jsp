<%@ page language="java" %>
<html>
	<head>
		<title> Login form </title>		
	</head>
	<body style="background-color: lightblue;">
		<div align ="center">
		<form name="Input" ENCTYPE="multipart/form-data" ACTION="Validate.jsp" METHOD=POST>
         	<table>
            	<tr>
               		<td>Upload an audio file:</td>
               		<td><input type = "file" name = "audio" accept="audio/*"></td>
            	</tr>	
		</table>
         	<br>
		<input type = 'submit' value = 'submit'>
      		</form>
     	 	</div>
   	</body>
</html>


