/**
 * 
 */
package com.book.utils;
import java.util.Map;
import org.apache.commons.beanutils.BeanUtils;

/**  
* @ClassName: WebUtils  
* @Description: BeanUtils 工具类，将网页传过来的属性封装到Map中，最后注入到Bean中
* @author lye  
* @date Nov 13, 2021    
*/
public class WebUtils {
	
	//此处第一个参数也可以是HTTPServletRequest 但是考虑到Dao层和Service层的可用性，应该使用Map耦合性更高
	public static <T> T copyParamToBean( Map value, T bean) {
		
		try {
			System.out.println("注入之前 " + bean);
			BeanUtils.populate(bean, value);
			System.out.println("注入之后 " + bean);
		} catch (Exception e) {
			
//			e.printStackTrace();
		}
		return bean;
	}
	
	public static int parseInt(String strInt, int defaultValue) {
		try {
			return Integer.parseInt(strInt);
		}catch (Exception e) {
			e.printStackTrace();
		}
		return defaultValue;
	}

}
