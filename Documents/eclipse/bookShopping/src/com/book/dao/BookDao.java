/**
 * 
 */
package com.book.dao;

import java.util.List;

import com.book.pojo.Book;

/**  
* @ClassName: BookDao  
* @Description: TODO 
* @author lye  
* @date Nov 13, 2021    
*/
public interface BookDao {
	public int addBook(Book book);
	public int deleteBookById(Integer id);
	public int updateBook(Book book);
	
	public Book queryBookById(Integer id);
	
	public List<Book> queryBooks();

	public Integer queryForPageTotalCount();
	
	public List<Book> queryForPageItems(int begin, int pageSize);

	public Integer queryForPageTotalCountByPrice(int min, int max);

	public List<Book> queryForPageItemsByPrice(int begin, int pageSize, int min, int max);
	

}
