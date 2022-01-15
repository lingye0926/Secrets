/**
 * 
 */
package com.book.web;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.book.pojo.User;
import com.book.service.UserService;
import com.book.service.impl.UserServiceImpl;

/**  
* @ClassName: LoginServlet  
* @Description: TODO 
* @author lye  
* @date Nov 12, 2021    
*/
public class LoginServlet extends HttpServlet{
	
	UserService userService = new UserServiceImpl();

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1 获取请求参数
		String username = req.getParameter("username");
		String password = req.getParameter("password");
		//2.调用userService.login()处理业务
		User loginUser = userService.login(new User(null, username, password, null));
		//如果等于null ,说明登录失败
		if(loginUser == null) {
			//把错误信息，和回显的表单项信息，保存到Request域中
			req.setAttribute("msg", "用户名或密码错误！");
			req.setAttribute("username", username);
			
			//跳回登录页面
			req.getRequestDispatcher("/pages/user/login.jsp").forward(req, resp);
		}else {
			//登录成功
			req.getRequestDispatcher("/pages/user/login_success.jsp").forward(req, resp);
		}
		
	}
	

}
