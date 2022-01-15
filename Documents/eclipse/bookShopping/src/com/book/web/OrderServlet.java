/**
 * 
 */
package com.book.web;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.book.pojo.Cart;
import com.book.pojo.User;
import com.book.service.OrderService;
import com.book.service.impl.OrderServiceImpl;
import com.book.utils.JdbcUtils;

/**  
* @ClassName: OrderServlet  
* @Description: TODO 
* @author lye  
* @date Dec 20, 2021    
*/
public class OrderServlet extends BaseServlet {
	private OrderService orderService = new OrderServiceImpl();

	protected void createOrder(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//线获取Cart购物车对象
		Cart cart = (Cart)req.getSession().getAttribute("cart");
		//获取UserId
		User loginUser = (User)req.getSession().getAttribute("user");
		
		if(loginUser == null) {
			req.getRequestDispatcher("/pages/user/login.jsp").forward(req, resp);
			return;
		}
		
		System.out.println("OrderServlet程序在【" + Thread.currentThread().getName() + "】中");
		
		Integer userId = loginUser.getId();
		//调用orderService的createOrder方法
		String orderId = orderService.createOrder(cart, userId);
	
		req.getSession().setAttribute("orderId", orderId);
//		req.setAttribute("orderId", orderId);
//		//请求转发到 http://localhost:8080/book/pages/cart/checkout.jsp
//		req.getRequestDispatcher("/pages/cart/checkout.jsp").forward(req, resp);
		
		resp.sendRedirect(req.getContextPath() + "/pages/cart/checkout.jsp");
		
	}
	
	

}
