/**
 * 
 */
package com.book.dao;

import com.book.pojo.User;

/**
 * 处理User数据库的接口
 * @author lye
 *
 */
public interface UserDao {
	
	
	//* 根据用户名查询用户信息，如果返回null，说明这个用户不存在，反之亦然。
	public User queryUserByUserName(String username);
	
	//保存用户信息，返回-1表示失败，返回其他数字是sql语句影响的行数
	public int saveUser(User user);
	
	//根据用户名和密码查询用户，如果返回null，说明这个用户名或密码错误，反之亦然。
	public User queryUserByUsernameAndPassword(String username,String password);

}
