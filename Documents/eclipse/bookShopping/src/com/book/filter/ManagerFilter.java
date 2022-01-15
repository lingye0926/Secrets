package com.book.filter;

import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import com.book.service.UserService;
import com.book.service.impl.UserServiceImpl;


public class ManagerFilter implements Filter {
	UserService userService = new UserServiceImpl();
	
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		
		HttpServletRequest httpServletRequest = (HttpServletRequest) request;
		HttpSession session = httpServletRequest.getSession();
		Object username = session.getAttribute("user");
		
		if(username == null) {
			request.getRequestDispatcher("/pages/user/login.jsp").forward(request, response);
		}else {
			chain.doFilter(request, response);
		}
		
	}



}
