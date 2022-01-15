/**
 * 
 */
package com.book.test;

import static org.junit.Assert.*;

import java.math.BigDecimal;
import java.util.Date;

import org.junit.Test;

import com.book.dao.OrderDao;
import com.book.dao.OrderDaoImpl;
import com.book.pojo.Order;

/**  
* @ClassName: OrderDaoTest  
* @Description: TODO 
* @author lye  
* @date Nov 24, 2021    
*/
public class OrderDaoTest {

	/**
	 * Test method for {@link com.book.dao.OrderDao#saveOrder(com.book.pojo.Order)}.
	 */
	@Test
	public void testSaveOrder() {
		OrderDao dao = new OrderDaoImpl();
		Order order = new Order("1234432",new Date(),new BigDecimal(78.65),0,1);
		dao.saveOrder(order);
	}

}
