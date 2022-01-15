/**
 * 
 */
package com.book.test;

import static org.junit.Assert.*;

import org.junit.Test;

import com.book.pojo.User;
import com.book.service.UserService;
import com.book.service.impl.UserServiceImpl;

/**  
* @ClassName: UserServiceImplTest  
* @Description: TODO 
* @author lye  
* @date Nov 12, 2021    
*/
public class UserServiceImplTest {
	UserService userService = new UserServiceImpl();
	
	@Test
	public void testRegistUser() {
		userService.registUser(new User(null,"bbj168","666666","bbj168@qq.com"));
		userService.registUser(new User(null,"abc168","888888","abc168@qq.com"));
	}

	
	@Test
	public void testLogin() {
		User login = userService.login(new User(null, "lisi", "lisi01", "lisi01@atbook.com"));
		if(login == null) {
			System.out.println("用户尚未登录");
		}else {
			System.out.println("用户已登录");
		}
	}

	
	@Test
	public void testExistsUsername() {
		if(userService.existsUsername("bbj169")) {
			System.out.println("用户名尚未注册");
		}else {
			System.out.println("用户名已存在");
		}
	}

}
