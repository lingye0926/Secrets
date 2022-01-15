/**
 * 
 */
package com.book.service.impl;

import com.book.dao.UserDao;
import com.book.dao.UserDaoImpl;
import com.book.pojo.User;
import com.book.service.UserService;

/**
 * @author lye
 *
 */
public class UserServiceImpl implements UserService{
	
	private UserDao userDao = new UserDaoImpl();

	@Override
	public void registUser(User user) {
		userDao.saveUser(user);
		
	}

	@Override
	public User login(User user) {
		return userDao.queryUserByUsernameAndPassword(user.getUsername(), user.getPassword());
		
	}

	@Override
	public boolean existsUsername(String username) {
		if(userDao.queryUserByUserName(username) == null) {
			return false;
		}
		return true;
	}

}
