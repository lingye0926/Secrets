/**
 * 
 */
package com.book.web;

import java.io.IOException;
import java.lang.reflect.Method;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**  
* @ClassName: BaseServlet  
* @Description: TODO 
* @author lye  
* @date Nov 13, 2021    
*/
public abstract class BaseServlet extends HttpServlet {
	
	
	
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		doPost(req, resp);
	}

	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String action = req.getParameter("action");
		
//		System.out.println(action);
		try {
			//获取action业务鉴别字符串，获取相应的业务 方法反射对象
			Method method = this.getClass().getDeclaredMethod(action,HttpServletRequest.class,HttpServletResponse.class);
//			System.out.println(method);
			//调用目标业务对应的方法
			method.invoke(this,req,resp);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);//把异常抛给Filter过滤器
		}
	}

}
