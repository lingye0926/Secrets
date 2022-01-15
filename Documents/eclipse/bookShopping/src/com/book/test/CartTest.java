/**
 * 
 */
package com.book.test;

import static org.junit.Assert.*;

import java.math.BigDecimal;

import org.junit.Test;

import com.book.pojo.Cart;
import com.book.pojo.CartItem;
import com.book.service.OrderService;
import com.book.service.impl.OrderServiceImpl;

/**  
* @ClassName: CartTest  
* @Description: TODO 
* @author lye  
* @date Nov 23, 2021    
*/
public class CartTest {
	
	Cart cart = new Cart();

	/**
	 * Test method for {@link com.book.pojo.Cart#addItem(com.book.pojo.CartItem)}.
	 */
	@Test
	public void testAddItem() {
		cart.addItem(new CartItem(1,"java从入门到精通",1,new BigDecimal(1000),new BigDecimal(1000)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.addItem(new CartItem(1,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		System.out.println(cart);
	}

	/**
	 * Test method for {@link com.book.pojo.Cart#deleteItem(java.lang.Integer)}.
	 */
	@Test
	public void testDeleteItem() {
		cart.addItem(new CartItem(1,"java从入门到精通",1,new BigDecimal(1000),new BigDecimal(1000)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.deleteItem(2);
		System.out.println(cart);
	}

	/**
	 * Test method for {@link com.book.pojo.Cart#clear()}.
	 */
	@Test
	public void testClear() {
		cart.addItem(new CartItem(1,"java从入门到精通",1,new BigDecimal(1000),new BigDecimal(1000)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.clear();
		System.out.println(cart);
	}

	/**
	 * Test method for {@link com.book.pojo.Cart#update(java.lang.Integer, java.lang.Integer)}.
	 */
	@Test
	public void testUpdate() {
		cart.addItem(new CartItem(1,"java从入门到精通",1,new BigDecimal(1000),new BigDecimal(1000)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.update(1, 10);
		System.out.println(cart);
	}
	
	@Test
	public void createOrder() {
		cart.addItem(new CartItem(1,"java从入门到精通",1,new BigDecimal(1000),new BigDecimal(1000)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		cart.addItem(new CartItem(2,"数据结构与算法",1,new BigDecimal(100),new BigDecimal(100)));
		OrderService orderService = new OrderServiceImpl();
		
		System.out.println(orderService.createOrder(cart, 1));
	}

}
