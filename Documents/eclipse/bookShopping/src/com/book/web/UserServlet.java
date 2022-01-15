package com.book.web;

import java.io.IOException;
import static com.google.code.kaptcha.Constants.KAPTCHA_SESSION_KEY;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.beanutils.BeanUtils;

import com.book.pojo.User;
import com.book.service.UserService;
import com.book.service.impl.UserServiceImpl;
import com.book.utils.WebUtils;


public class UserServlet extends BaseServlet{
	
	//使用hidden表单整合Login和Register业务到一个服务器UserServlet
	UserService userService = new UserServiceImpl();
	
	//处理登录的功能
	protected void login(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
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
			//保存用户登录之后的信息到session
			req.getSession().setAttribute("user", loginUser);
			req.getRequestDispatcher("/pages/user/login_success.jsp").forward(req, resp);
		}
	}
	
	//处理注册的功能
	protected void regist(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
		//处理注册的需求
		//获取请求参数
		String username = req.getParameter("username");
		String password = req.getParameter("password");
		String email = req.getParameter("email");
		String code = req.getParameter("code");
		String token = (String)req.getSession().getAttribute(KAPTCHA_SESSION_KEY);
		
		User user =  WebUtils.copyParamToBean(req.getParameterMap(), new User());
		
		//检查 验证码是否正确  ==写死，要求验证码为：abcde
		if(token !=null && token.equalsIgnoreCase(code)) {
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
	//用户注销
	protected void logOut(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
		//1 销毁session中的用户信息
		req.getSession().invalidate();
		//2 重定向到首页（或者登录页面）
		resp.sendRedirect(req.getContextPath());
	}

}
