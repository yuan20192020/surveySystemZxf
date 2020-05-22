from django.template import loader

from rest_framework import serializers

from web import models


class SurveySerializer(serializers.ModelSerializer):

#	grade = serializers.CharField(source="grade.name",write_only=True)	
	valid_count = serializers.SerializerMethodField()
	handle_link = serializers.SerializerMethodField()
	handle = serializers.SerializerMethodField()
	date = serializers.DateTimeField(format="%Y-%m-%d %X")

	class Meta:
		model = models.Survey
		#fields = "__all__"
		fields = (
			"grade",
			"times",
			"valid_count",
			"handle_link",
			"date",
			"handle"
		)

	def get_valid_count(self, instance):
		'''
		获取有效的填写人次
		'''
		return models.SurveyCode.objects.filter(survey=instance, is_used=True).count()

	def get_handle_link(self, instance):
		'''
		获取填写的链接
		'''
		request = self.context.get("request")	
		return f"{request.scheme}://{request.get_host()}/{instance.pk}"
		#return "http://xiaofang.website:7777/{instance.pk}"

	def get_handle(self, instance):

		return loader.render_to_string(
			"web/components/handle.html",
			context={
				"report_link": "",
				"download_link": ""
			}
		) 
