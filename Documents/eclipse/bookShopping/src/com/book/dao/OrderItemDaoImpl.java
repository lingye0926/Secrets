/**
 * 
 */
package com.book.dao;

import com.book.pojo.OrderItem;

/**  
* @ClassName: OrderItemDaoImpl  
* @Description: TODO 
* @author lye  
* @date Nov 24, 2021    
*/
public class OrderItemDaoImpl extends BaseDao implements OrderItemDao{

	@Override
	public int saveOrderItem(OrderItem orderItem) {
		System.out.println("OrderItemDaoImpl程序在【" + Thread.currentThread().getName() + "】中");
		String sql = "insert into t_order_item (name,count,price,total_price,order_id) values(?,?,?,?,?)";
		return update(sql, orderItem.getName(),orderItem.getCount(),orderItem.getPrice(),orderItem.getTotalPrice(),orderItem.getOrderId());
	}

}
