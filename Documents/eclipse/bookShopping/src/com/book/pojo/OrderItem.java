/**
 * 
 */
package com.book.pojo;

import java.math.BigDecimal;

/**  
* @ClassName: OrderIten  
* @Description: TODO 
* @author lye  
* @date Nov 24, 2021    
*/
public class OrderItem {
	
	private Integer id;
	private String name;
	private Integer count;
	private BigDecimal price;
	private BigDecimal totalPrice;
	private String OrderId;
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Integer getCount() {
		return count;
	}
	public void setCount(Integer count) {
		this.count = count;
	}
	public BigDecimal getPrice() {
		return price;
	}
	public void setPrice(BigDecimal price) {
		this.price = price;
	}
	public BigDecimal getTotalPrice() {
		return totalPrice;
	}
	public void setTotalPrice(BigDecimal totalPrice) {
		this.totalPrice = totalPrice;
	}
	public String getOrderId() {
		return OrderId;
	}
	public void setOrderId(String orderId) {
		OrderId = orderId;
	}
	public OrderItem(Integer id, String name, Integer count, BigDecimal price, BigDecimal totalPrice, String orderId) {
		super();
		this.id = id;
		this.name = name;
		this.count = count;
		this.price = price;
		this.totalPrice = totalPrice;
		OrderId = orderId;
	}
	public OrderItem() {
		super();
	}
	@Override
	public String toString() {
		return "OrderItem [id=" + id + ", name=" + name + ", count=" + count + ", price=" + price + ", totalPrice="
				+ totalPrice + ", OrderId=" + OrderId + "]";
	}
	
	
	
}
