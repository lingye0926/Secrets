package com.book.test;

import static org.junit.Assert.*;

import java.math.BigDecimal;

import org.junit.Test;

import com.book.pojo.Book;
import com.book.pojo.Page;
import com.book.service.BookService;
import com.book.service.impl.BookServiceImpl;

public class BookServiceImplTest {
	private BookService bookService = new BookServiceImpl();

	@Test
	public void testAddBook() {
		bookService.addBook(new Book(null,"TCP/IP开发原理","郭老师",new BigDecimal(26.87),182,26,null));
	}

	@Test
	public void testDeleteBookById() {
		bookService.deleteBookById(12);
	}

	@Test
	public void testUpdateBook() {
		bookService.updateBook(new Book(8,"JavaEE全面开发","国哥",new BigDecimal(119.87),326,216,null));;
	}

	@Test
	public void testQueryBookById() {
		Book book = bookService.queryBookById(8);
		System.out.println(book);
	}

	@Test
	public void testQueryBooks() {
		System.out.println(bookService.queryBooks());
	}
	
	@Test
	public void testPage() {
		Page<Book> page = bookService.page(1, Page.PAGE_SIZE);
		System.out.println(page);
	}
	


}
