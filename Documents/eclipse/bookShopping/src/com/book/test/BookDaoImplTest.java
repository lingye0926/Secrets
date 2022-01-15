package com.book.test;

import static org.junit.Assert.*;

import java.math.BigDecimal;
import java.util.List;

import org.junit.Test;

import com.book.dao.BookDao;
import com.book.dao.BookDaoImpl;
import com.book.pojo.Book;
import com.book.pojo.Page;

public class BookDaoImplTest {
	
	BookDao bookDao = new BookDaoImpl();

	@Test
	public void testAddBook() {
		int addBook = bookDao.addBook(new Book(null, "没时间捡屎", "张大锤", new BigDecimal(19.9), 11, 2, "static/img/default.jpg"));
		System.out.println(addBook);
	}
	
	
	@Test
	public void testDeleteBookById() {
		fail("Not yet implemented");
	}
	
	
	@Test
	public void testUpdateBook() {

		bookDao.updateBook(new Book(9,"编程好难","超哥",new BigDecimal(78.98),193,88,null));
		bookDao.updateBook(new Book(13,"30天学会JavaScript","杨波",new BigDecimal(21.19),34,18,null));
		bookDao.updateBook(new Book(10,"Git命令大全","郭帅",new BigDecimal(9.98),13,8,null));
		
		
	
	}
	
	@Test
	public void testQueryBookById() {
		Book book = bookDao.queryBookById(1);
		System.out.println(book);
	}
	
	@Test
	public void testQueryBooks() {
		List<Book> queryBooks = bookDao.queryBooks();
		System.out.println(queryBooks);
	}
	
	@Test
	public void testQueryForPageTotalCount() {
		System.out.println(bookDao.queryForPageTotalCount());
	}
	
	@Test
	public void testQueryForPageItems() {
		System.out.println(bookDao.queryForPageItems(0, 4));
	}
	
	@Test
	public void testQueryForPageTotalCountByPrice() {
		System.out.println(bookDao.queryForPageTotalCountByPrice(10, 50));
	}
	
	@Test
	public void testQueryForPageItemsByPrice() {
		List<Book> list = bookDao.queryForPageItemsByPrice(0, Page.PAGE_SIZE, 10, 50);
		for(Book book:list) {
			System.out.println(book);
		}
	}
	

}
