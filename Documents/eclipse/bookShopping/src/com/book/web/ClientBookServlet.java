/**
 * 
 */
package com.book.web;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.book.pojo.Book;
import com.book.pojo.Page;
import com.book.service.BookService;
import com.book.service.impl.BookServiceImpl;
import com.book.utils.WebUtils;

/**  
* @ClassName: ClientBookServlet  
* @Description: TODO 
* @author lye  
* @date Nov 14, 2021    
*/
public class ClientBookServlet extends BaseServlet{
	BookService bookService = new BookServiceImpl();

	protected void page(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		//1.获取请求的参数pageNo和pageSize(此处一页显示多少数据由客户自己设置决定，还有一种方式是根据页面的数据大小而显示)
		int pageNo = WebUtils.parseInt(req.getParameter("pageNo"), 1);
		int pageSize = WebUtils.parseInt(req.getParameter("pageSize"), Page.PAGE_SIZE);
		//2.调用BookService.page(pageNo,pageSize)方法，返回Page对象
		Page<Book> page = bookService.page(pageNo,pageSize);
		page.setUrl("client/bookServlet?action=page");
		//3.保存Page对象到Reuqest域中
		req.setAttribute("page", page);
		//4.请求转发到/pages/manager/book_manager.jsp页面
		req.getRequestDispatcher("/pages/client/index.jsp").forward(req, resp);
	}
	
	protected void pageByPrice(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		//1.获取请求的参数pageNo和pageSize(此处一页显示多少数据由客户自己设置决定，还有一种方式是根据页面的数据大小而显示)
		int pageNo = WebUtils.parseInt(req.getParameter("pageNo"), 1);
		int pageSize = WebUtils.parseInt(req.getParameter("pageSize"), Page.PAGE_SIZE);
		int min = WebUtils.parseInt(req.getParameter("min"), 0);
		int max = WebUtils.parseInt(req.getParameter("max"), Integer.MAX_VALUE);
		//2.调用BookService.page(pageNo,pageSize)方法，返回Page对象
		Page<Book> page = bookService.pageByPrice(pageNo,pageSize,min,max);
		
		//如果有最小价格区间的参数，追加到分页条的地址参数中
		StringBuilder sb = new StringBuilder("client/bookServlet?action=pageByPrice");
		if(req.getParameter("min") != null) {
			sb.append("&min=").append(req.getParameter("min"));
		}
		//如果有最小价格区间的参数，追加到分页条的地址参数中
		if(req.getParameter("max") != null) {
			sb.append("&max=").append(req.getParameter("max"));
		}
		
		page.setUrl(sb.toString());
		//3.保存Page对象到Reuqest域中
		req.setAttribute("page", page);
		//4.请求转发到/pages/manager/book_manager.jsp页面
		req.getRequestDispatcher("/pages/client/index.jsp").forward(req, resp);
	}
}
