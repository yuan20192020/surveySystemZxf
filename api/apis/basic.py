from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework import pagination

from web import models

from ..serializers import basic

class SurveysApi(ListAPIView):
	'''
	获取一组数据需要什么：
		1.model
		2.序列化器

	'''	
	queryset = models.Survey.objects.all()
	#queryset = models.Survey.objects.filter(grade='1')
	serializer_class = basic.SurveySerializer
	
	filter_backends= [filters.SearchFilter, filters.OrderingFilter]
	#过滤器
	search_fields = ["grade__name", "times"]
	#排序
	ordering_fields=['grade__name','times']	
	#分页
	pagination_class = pagination.LimitOffsetPagination

	table_column = [{"prop":'grade',"label":'记录状态'},{"prop":'times',"label":'试模日期'},{"prop":'valid_count',"label":'机型'},{"prop":'handle_link',"label":'模号'},{"prop":'date',"label":'部门'},{"prop":'handle',"label":'模具类别'}]

	def get_paginated_response(self, data):
		return Response({
			"code": 0,
			"data": {
				"table_column":self.table_column,
				"table_data":{"total":self.paginator.count,"data": data}
			} 
		})


	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)
   
		serializer = self.get_serializer(queryset, many=True)
		return Response({
			"code": 0,
			"data":{
				"table_column":self.table_column,
				"table_data":serializer.data
			}
		})	
