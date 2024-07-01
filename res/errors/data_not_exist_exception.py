class Data_not_exist_exception(Exception):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)