/**
 * 
 */
package com.book.web;

import java.io.IOException;
import java.math.BigDecimal;
import java.util.List;

import javax.security.auth.message.callback.PrivateKeyCallback.Request;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.book.pojo.Book;
import com.book.pojo.Page;
import com.book.service.BookService;
import com.book.service.impl.BookServiceImpl;
import com.book.utils.WebUtils;

/**  
* @ClassName: BookServlet  
* @Description: TODO 
* @author lye  
* @date Nov 13, 2021    
*/
public class BookServlet extends BaseServlet{
	
	private BookService bookService = new BookServiceImpl();

	
	protected void add(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1.获取请求的参数并封装称为Book对象
		int pageNo = WebUtils.parseInt(req.getParameter("pageNo"), 0);
		pageNo+=1;
		Book book = WebUtils.copyParamToBean(req.getParameterMap(), new Book());
		
		//2.调用BookService的addBook()方法将Book对象添加到数据库
		bookService.addBook(book);
		//3.跳到图书列表页面--/manager/bookServlet?action=list
//		req.getRequestDispatcher("/manager/bookServlet?action=list").forward(req, resp);
		resp.sendRedirect(req.getContextPath()+ "/manager/bookServlet?action=page&pageNo=" + pageNo);
		
	}
	
	protected void delete(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1.获取请求参数id图书编号
		int id = WebUtils.parseInt(req.getParameter("id"),0);
		//2.调用BookService的deleteBookById()方法，删除图书
		bookService.deleteBookById(id);
		//3.请求重定向到图书列表页面--/manager/bookServlet?action=list
		resp.sendRedirect(req.getContextPath()+ "/manager/bookServlet?action=page&pageNo="+req.getParameter("pageNo"));
		
	}
	
	protected void getBook(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1.获取请求的参数图书编号
		int id = WebUtils.parseInt(req.getParameter("id"), 0);
		//2.调用BookService.queryBookById(id)查询图书
		Book book = bookService.queryBookById(id);
		//3.将获取的Book对象保存到request域中
		req.setAttribute("book", book);
		//4.请求转发到pages/manager/book_edit.jsp
		req.getRequestDispatcher("/pages/manager/book_edit.jsp").forward(req, resp);
		
	}
	
	protected void update(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1.获取请求的参数,并将其封装称为Book对象
		Book book = WebUtils.copyParamToBean(req.getParameterMap(), new Book());
		//2.调用BookService.update(book)把更新后的数据保存到数据库中
		bookService.updateBook(book);
		//3.请求重定向到图书列表页面--/manager/bookServlet?action=list
		resp.sendRedirect(req.getContextPath()+ "/manager/bookServlet?action=page&pageNo="+req.getParameter("pageNo"));
		
	}
	
	protected void list(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1.通过BookServlet查询全部图书
		List<Book> books = bookService.queryBooks();
		//2.把全部图书保存到Request域中
		req.setAttribute("books", books);
		
		//3.请求转发到/pages/manager/book_manager.jsp页面
		req.getRequestDispatcher("/pages/manager/book_manager.jsp").forward(req, resp);
	}
	
	protected void page(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1.获取请求的参数pageNo和pageSize(此处一页显示多少数据由客户自己设置决定，还有一种方式是根据页面的数据大小而显示)
		int pageNo = WebUtils.parseInt(req.getParameter("pageNo"), 1);
		int pageSize = WebUtils.parseInt(req.getParameter("pageSize"), Page.PAGE_SIZE);
		//2.调用BookService.page(pageNo,pageSize)方法，返回Page对象
		Page<Book> page = bookService.page(pageNo,pageSize);
		page.setUrl("manager/bookServlet?action=page");
		//3.保存Page对象到Reuqest域中
		req.setAttribute("page", page);
		//4.请求转发到/pages/manager/book_manager.jsp页面
		req.getRequestDispatcher("/pages/manager/book_manager.jsp").forward(req, resp);
	}
	
	

}
