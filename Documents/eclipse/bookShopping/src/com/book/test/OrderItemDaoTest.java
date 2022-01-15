/**
 * 
 */
package com.book.test;

import static org.junit.Assert.*;

import java.math.BigDecimal;

import org.junit.Test;

import com.book.dao.OrderItemDao;
import com.book.dao.OrderItemDaoImpl;
import com.book.pojo.OrderItem;

/**  
* @ClassName: OrderItemDaoTest  
* @Description: TODO 
* @author lye  
* @date Nov 24, 2021    
*/
public class OrderItemDaoTest {

	/**
	 * Test method for {@link com.book.dao.OrderItemDao#saveOrderItem(com.book.pojo.OrderItem)}.
	 */
	@Test
	public void testSaveOrderItem() {
		OrderItemDao dao = new OrderItemDaoImpl();
		dao.saveOrderItem(new OrderItem(null,"java从入门到精通",1,new BigDecimal(100),new BigDecimal(100),"1234432"));
		dao.saveOrderItem(new OrderItem(null,"javaScript从入门到精通",1,new BigDecimal(100),new BigDecimal(100),"1234432"));
		dao.saveOrderItem(new OrderItem(null,"SQL从入门到精通",1,new BigDecimal(100),new BigDecimal(100),"1234432"));
		
	}

}
