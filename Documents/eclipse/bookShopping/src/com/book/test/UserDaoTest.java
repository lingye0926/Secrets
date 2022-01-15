/**
 * 
 */
package com.book.test;

import org.junit.Test;

import com.book.dao.UserDao;
import com.book.dao.UserDaoImpl;
import com.book.pojo.User;

/**
 * @author lye
 *
 */
public class UserDaoTest {
	UserDao dao = new UserDaoImpl();
	
	@Test
	public void queryUserByUserName() {
		
		User user = dao.queryUserByUserName("admin");
		System.out.println(user);
		
	}
	
	@Test
	public void  saveUser() {
		User user = new User(null, "lisi", "lisi01", "lisi01@atbook.com");
		int saveUser = dao.saveUser(user);
		System.out.println(saveUser);
		
		
	}
	
	@Test
	public void queryUserByUsernameAndPassword() {
		User user = dao.queryUserByUsernameAndPassword("lisi", "lisi01");
		System.out.println(user);
		
	}

}