/**
 * 
 */
package com.book.service.impl;

import java.util.Date;
import java.util.Map;

import com.book.dao.BookDao;
import com.book.dao.BookDaoImpl;
import com.book.dao.OrderDao;
import com.book.dao.OrderDaoImpl;
import com.book.dao.OrderItemDao;
import com.book.dao.OrderItemDaoImpl;
import com.book.pojo.Book;
import com.book.pojo.Cart;
import com.book.pojo.CartItem;
import com.book.pojo.Order;
import com.book.pojo.OrderItem;
import com.book.service.OrderService;

/**  
* @ClassName: OrderServiceImpl  
* @Description: TODO 
* @author lye  
* @date Dec 9, 2021    
*/
public class OrderServiceImpl implements OrderService{
	
	private OrderDao orderDao = new OrderDaoImpl();
	private OrderItemDao orderItemDao = new OrderItemDaoImpl();
	private BookDao bookDao = new BookDaoImpl();

	@Override
	public String createOrder(Cart cart, Integer userId) {
		System.out.println("OrderServiceImpl程序在【" + Thread.currentThread().getName() + "】中");
		//订单号---唯一性
		String orderId = System.currentTimeMillis() + "" + userId;
		//创建一个订单对象
		Order order = new Order(orderId,new Date(),cart.getTotalPrice(),0,userId);
		//保存订单
		orderDao.saveOrder(order);
		
		int i = 12/0;
		
		//遍历购物车中每一个商品项转化成为订单项保存到数据库
		 
		for(Map.Entry<Integer, CartItem> entry: cart.getItems().entrySet()) {
			//获取每一个购物车中的商品项
			CartItem cartItem = entry.getValue();
			//转化为每一个订单项
			OrderItem orderItem = new OrderItem(null,cartItem.getName(),cartItem.getCount(),cartItem.getPrice(),cartItem.getTotalPrice(),orderId);
			//保存订单项到数据库
			orderItemDao.saveOrderItem(orderItem);
			Book book = bookDao.queryBookById(cartItem.getId());
			book.setSales(book.getSales() + cartItem.getCount());
			book.setStock(book.getStock() - cartItem.getCount());
			bookDao.updateBook(book);
		}
		cart.clear();
		return orderId;
	}

}
