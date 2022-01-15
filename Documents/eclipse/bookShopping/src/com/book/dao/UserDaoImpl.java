/**
 * 
 */
package com.book.dao;

import com.book.pojo.User;
import com.book.test.UserDaoTest;

/**
 * @author lye
 *
 */
public class UserDaoImpl extends BaseDao implements UserDao{

	@Override
	public User queryUserByUserName(String username) {
		String sql = "select `id`,username,`password`,email from t_user where username = ?";
		
		return queryForOne(User.class, sql, username);
	}

	@Override
	public int saveUser(User user) {
		String sql = "insert into t_user(`username`,`password`,email) values(?,?,?)";
		return update(sql, user.getUsername(),user.getPassword(),user.getEmail());
	}

	@Override
	public User queryUserByUsernameAndPassword(String username, String password) {
		String sql = "select `id`,username,`password`,email from t_user where username = ? and password = ?";
		return queryForOne(User.class, sql, username,password);
	}

}
