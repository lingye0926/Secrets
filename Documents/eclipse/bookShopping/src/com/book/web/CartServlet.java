/**
 * 
 */
package com.book.web;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.book.pojo.Book;
import com.book.pojo.Cart;
import com.book.pojo.CartItem;
import com.book.service.BookService;
import com.book.service.impl.BookServiceImpl;
import com.book.utils.WebUtils;

/**  
* @ClassName: CartServlet  
* @Description: TODO 
* @author lye  
* @date Nov 23, 2021    
*/
public class CartServlet extends BaseServlet{
	private BookService bookService = new BookServiceImpl();
	
	//更新商品数量
	protected void updateCount(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//获取请求的参数 商品编号  商品商量
		int id = WebUtils.parseInt(req.getParameter("id"), 0);
		int count = WebUtils.parseInt(req.getParameter("count"), 0);
		//获取cart购物车对象
		Cart cart = (Cart)req.getSession().getAttribute("cart");
		
		if(cart != null) {
			//修改商品数量
			cart.update(id, count);
			//重定向回修改页面
			resp.sendRedirect(req.getHeader("Referer"));
		}
		
	}
	
	//清空购物车
	protected void clear(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//获取购物车对象
		Cart cart = (Cart)req.getSession().getAttribute("cart");
		if(cart != null) {
			//清空购物车
			cart.clear();
			//重定向回清空按钮页面
			resp.sendRedirect(req.getHeader("Referer"));
		}
		
	}
	
	//删除商品项
	protected void deleteItem(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		int id = WebUtils.parseInt(req.getParameter("id"), 0);
		Cart cart = (Cart)req.getSession().getAttribute("cart");
		if(cart != null) {
			//删除指定项
			cart.deleteItem(id);
			//重定向回删除页面
			resp.sendRedirect(req.getHeader("Referer"));
		}
	}
		
	
	//加入购物车
	protected void addItem(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		
		//获取请求的参数：商品编号
		int id = WebUtils.parseInt(req.getParameter("id"), 0);
		//调用bookService.queryBookById(id):Book得到商品图书的信息
		Book book = bookService.queryBookById(id);
		//把图书信息转化成为cartItem商品项
		CartItem cartItem = new CartItem(book.getId(),book.getName(),1,book.getPrice(),book.getPrice());
		//调用Cart.addItem(CartItem)添加商品项
		Cart cart = (Cart)req.getSession().getAttribute("cart");
		if(cart == null) {
			cart = new Cart();
			req.getSession().setAttribute("cart", cart);
		}
		cart.addItem(cartItem);
		System.out.println(cart);
		//重定向回商品列表页面
		System.out.println("请求头Referer的值：" + req.getHeader("Referer"));
		resp.sendRedirect(req.getHeader("Referer"));
		req.getSession().setAttribute("lastName", cartItem.getName());
	}

}
