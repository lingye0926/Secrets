<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
    <%
    	String basePath = request.getScheme()
	    	+"://"
	    	+ request.getServerName()
	    	+ ":"
	    	+ request.getServerPort()
	    	+ request.getContextPath()
	    	+"/";
		pageContext.setAttribute("basePath", basePath);
    %>
    
    
   <%--  <%=basePath%> --%>
		<!-- 写base标签，永远固定相对路径跳转的结果 -->
		<base href="<%=basePath%>">
		<link type="text/css" rel="stylesheet" href="static/css/style.css" >
		<script type="text/javascript" src="static/script/jquery-1.7.2.js"></script> 
		<!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script> --> 