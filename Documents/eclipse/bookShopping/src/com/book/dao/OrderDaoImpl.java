/**
 * 
 */
package com.book.dao;

import com.book.pojo.Order;
import com.book.utils.JdbcUtils;

/**  
* @ClassName: OrderDaoImpl  
* @Description: TODO 
* @author lye  
* @date Nov 24, 2021    
*/
public class OrderDaoImpl extends BaseDao implements OrderDao{

	@Override
	public int saveOrder(Order order) {
		System.out.println("OrderDaoImpl程序在【" + Thread.currentThread().getName() + "】中");
		String sql = "insert into t_order (order_id,create_time,price,status,user_id) values(?,?,?,?,?)";
		int update = update(sql, order.getOrderId(),order.getCreateTime(),order.getPrice(),order.getStatus(),order.getUserId());
		return update;
	}

}
