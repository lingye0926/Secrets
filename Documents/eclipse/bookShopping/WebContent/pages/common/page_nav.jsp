<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
		<!-- 分页条的开始-->
		<div id="page_nav">
			<!-- 只有页码大于1的时候才显示上一页和首页-->
			<c:if test="${requestScope.page.pageNo > 1}">
				<a href="${requestScope.page.url}&pageNo=1">首页</a>
				<a
					href="${requestScope.page.url}&pageNo=${requestScope.page.pageNo-1}">上一页</a>
			</c:if>


			<%--页码输出的开始--%>
			<c:choose>
				<%--情况1 ：假如总页码小于5,页码的范围为:1~总页码 --%>
				<c:when test="${requestScope.page.pageTotal <= 5}">
					<c:set var="begin" value="1"></c:set>
					<c:set var="end" value="${requestScope.page.pageTotal}"></c:set>
				</c:when>
				<%--情况2 ：假如总页码大于5--%>
				<c:when test="${requestScope.page.pageTotal > 5}">
					<c:choose>
						<%--小情况1：当前页码为1 2 3的情况,页码的范围为: 1 ~ 5 --%>
						<c:when test="${requestScope.page.pageNo <= 3}">
							<c:set var="begin" value="1"></c:set>
							<c:set var="end" value="5"></c:set>
						</c:when>
						<%--小情况2：页码为8,9,10的情况,页码的范围为：总页码-4 ~总页码 --%>
						<c:when
							test="${requestScope.page.pageNo >= requestScope.page.pageTotal-3}">
							<c:set var="begin" value="${requestScope.page.pageTotal-4}"></c:set>
							<c:set var="end" value="${requestScope.page.pageTotal}"></c:set>
						</c:when>
						<%--小情况3：页码为4,5,6,7的情况，页码的范围为：当前页码-2~当前页码+2 --%>
						<c:otherwise>
							<c:set var="begin" value="${requestScope.page.pageNo-2}"></c:set>
							<c:set var="end" value="${requestScope.page.pageNo + 2}"></c:set>
						</c:otherwise>
					</c:choose>
				</c:when>
			</c:choose>

			<c:forEach begin="${begin}" end="${end}" var="i">
				<%--i是当前页码--%>
				<c:if test="${i == requestScope.page.pageNo}">
            		【${i}】
        		</c:if>
				<%--i不是当前页码--%>
				<c:if test="${i != requestScope.page.pageNo}">
					<a href="${requestScope.page.url}&pageNo=${i}">${i}</a>
				</c:if>
			</c:forEach>


			<%--页码输出的结束--%>


			<!-- 只有页码小于最后一页的时候才显示下一页和末页 -->
			<c:if
				test="${requestScope.page.pageNo < requestScope.page.pageTotal}">
				<a
					href="${requestScope.page.url}&pageNo=${requestScope.page.pageNo+1}">下一页</a>
				<a
					href="${requestScope.page.url}&pageNo=${requestScope.page.pageTotal}">末页</a>
			</c:if>

			共${requestScope.page.pageTotal}页,${requestScope.page.pageTotalCount}条记录
			到第<input value="${param.pageNo}" name="pn" id="pn_input" />页 <input
				id="searchPageBtn" type="button" value="确定">
			<script type="text/javascript">
				$(function(){
					$("#searchPageBtn").click(function(){
						var pageNo = $("#pn_input").val();
						var totalPage = ${requestScope.page.pageTotal};
						if(pageNo < 0 || pageNo > totalPage ){
							alert("非法的页面数值");
						}else{
							location.href = "${pageScope.basePath}${requestScope.page.url}&pageNo=" + pageNo;
						}
					});
				});
			</script>
		</div>
		<!-- 分页条的结束 -->