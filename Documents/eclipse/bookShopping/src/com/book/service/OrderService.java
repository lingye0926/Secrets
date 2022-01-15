/**
 * 
 */
package com.book.service;

import com.book.pojo.Cart;

/**  
* @ClassName: OrderService  
* @Description: TODO 
* @author lye  
* @date Nov 24, 2021    
*/
public interface OrderService {
	public String createOrder(Cart cart,Integer userId);
}
