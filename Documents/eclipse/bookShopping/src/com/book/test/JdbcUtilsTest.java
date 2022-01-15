package com.book.test;

import org.junit.Test;

import com.book.utils.JdbcUtils;

public class JdbcUtilsTest {
	
	@Test
	public void testJdbcUtils() {
		for (int i = 0; i < 100; i++) {
			System.out.println(JdbcUtils.getConnection());
		}
	}

}
