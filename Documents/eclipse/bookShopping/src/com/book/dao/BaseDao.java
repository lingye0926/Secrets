package com.book.dao;

import java.sql.Connection;
import java.util.List;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

import com.book.utils.JdbcUtils;

public abstract class BaseDao {
	//使用DBUtils操作数据库
	private QueryRunner queryRunner = new QueryRunner();
	
	/*
	 * Update方法用来执行：Insert/Update/Delete语句
	 */
	
	public int update(String sql,Object...args) {
		System.out.println("BaseDao程序在【" + Thread.currentThread().getName() + "】中");
		Connection conn = new JdbcUtils().getConnection();
		try {
			return queryRunner.update(conn, sql, args);
		}catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
	
	/*
	 * 查询返回一个Javabean的sql语句
	 */
	public <T>T queryForOne(Class<T> type ,String sql,Object...args) {
		Connection conn = new JdbcUtils().getConnection();
		try {
			return queryRunner.query(conn,sql, new BeanHandler<T>(type), args);
		}catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
		
	}
	/*
	 * 查询返回多个JavaBean List的sql语句
	 */
	
	public <T>List<T> queryForList(Class<T> type,String sql, Object...args){
		Connection conn = JdbcUtils.getConnection();
		try {
			return queryRunner.query(conn, sql,new BeanListHandler<T>(type),args);
		}catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
	
	/*
	 * 执行返回一行一列的sql语句
	 * 
	 */
	public Object queryForSingleValue(String sql,Object...args) {
		Connection conn = JdbcUtils.getConnection();
		try {
			return queryRunner.query(conn, sql, new ScalarHandler(), args);
		}catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
	
}
