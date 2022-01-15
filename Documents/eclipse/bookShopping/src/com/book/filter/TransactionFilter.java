/**
 * 
 */
package com.book.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

import com.book.utils.JdbcUtils;

/**  
* @ClassName: TransactionFilter  
* @Description: TODO 
* @author lye  
* @date Dec 25, 2021    
*/
public class TransactionFilter implements Filter {

	@Override
	public void destroy() {
		// TODO Auto-generated method stub
		Filter.super.destroy();
	}

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) {
		
		try {
			chain.doFilter(request, response);
			JdbcUtils.commitAndClose();
		} catch (Exception e) {
			JdbcUtils.rollBackAndClose();
			e.printStackTrace();
			throw new RuntimeException(e);//把异常抛给tomcat管理展示友好的错误页面

		}
	}

	@Override
	public void init(FilterConfig filterConfig) throws ServletException {
		// TODO Auto-generated method stub
		Filter.super.init(filterConfig);
	}

}
