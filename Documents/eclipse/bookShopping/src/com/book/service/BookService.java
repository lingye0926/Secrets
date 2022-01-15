/**
 * 
 */
package com.book.service;

import java.util.List;

import com.book.pojo.Book;
import com.book.pojo.Page;

/**  
* @ClassName: BookService  
* @Description: TODO 
* @author lye  
* @date Nov 13, 2021    
*/
public interface BookService {
	
	public void addBook(Book book);
	public void deleteBookById(Integer id);
	public void updateBook(Book book);
	
	public Book queryBookById(Integer id);
	
	public List<Book> queryBooks();

	public Page<Book> page(int pageNo, int pageSize);

	public Page<Book> pageByPrice(int pageNo, int pageSize, int min, int max);

}
