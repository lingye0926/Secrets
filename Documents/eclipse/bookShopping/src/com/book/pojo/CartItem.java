/**
 * 
 */
package com.book.pojo;

import java.math.BigDecimal;

/**  
* @ClassName: CartItem 购物车  
* @Description: TODO 
* @author lye  
* @date Nov 23, 2021    
*/
public class CartItem {
	private Integer id;
	private String name;
	private Integer count;
	private BigDecimal price;
	private BigDecimal totalPrice;
	
	
	public CartItem() {
		super();
	}
	
	public CartItem(Integer id, String name, Integer count, BigDecimal price, BigDecimal totalPrice) {
		super();
		this.id = id;
		this.name = name;
		this.count = count;
		this.price = price;
		this.totalPrice = totalPrice;
	}

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

	@Override
	public String toString() {
		return "CartItem [id=" + id + ", name=" + name + ", count=" + count + ", price=" + price + ", totalPrice="
				+ totalPrice + "]";
	}
	
	

}
