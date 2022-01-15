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
* @ClassName: RegistServlet  
* @Description: TODO 
* @author lye  
* @date Nov 12, 2021    
*/
public class RegistServlet extends HttpServlet{
	UserService userService = new UserServiceImpl();

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//获取请求参数
		String username = req.getParameter("username");
		String password = req.getParameter("password");
		String email = req.getParameter("email");
		String code = req.getParameter("code");
		
		//检查 验证码是否正确  ==写死，要求验证码为：abcde
		if("abcde".equalsIgnoreCase(code)) {
			//正确：
			//检查用户名是否可用
			boolean existsUsername = userService.existsUsername(username);
			if(existsUsername) {
				//不可用，用户名已存在
				//把回显信息，保存到request域中
				req.setAttribute("msg", "用户名已存在！");
				req.setAttribute("username", username);
				req.setAttribute("email", email);
				//跳回注册页面
				req.getRequestDispatcher("/pages/user/regist.jsp").forward(req, resp);
			}else {
				//可用
				//调用service保存到数据库
				userService.registUser(new User(null,username,password,email));
				req.getRequestDispatcher("/pages/user/regist_success.jsp").forward(req, resp); 
			}
			
		}else {
			//不正确 跳回到注册页面
			//把回显信息，保存到request域中
			req.setAttribute("msg", "验证码错误");
			req.setAttribute("username", username);
			req.setAttribute("email", email);
			
			System.out.println("验证码" + code + "错误");
			req.getRequestDispatcher("/pages/user/regist.jsp").forward(req, resp);
		}
		
		
	}
	
	

}
