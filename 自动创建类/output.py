class BaseModule:
	def __init__(self, _json):
		self.paras = {
			"name":"",
			"style":"",
			"bubble_type":"",
			"bubble_style":"",
			"is_necessary":"",
			"is_changeable":"",
			"c_float_range":"",
			"a_float_range":"",
			"cost_per_square":"",
			"area":"",
			"cost":"",
			"geos":"",
			}

		@property
		def name(self):
			return self.paras["name"]

		@name.setter
		def name(self, name):
			self.paras["name"] = name


		@property
		def style(self):
			return self.paras["style"]

		@style.setter
		def style(self, style):
			self.paras["style"] = style


		@property
		def bubble_type(self):
			return self.paras["bubble_type"]

		@bubble_type.setter
		def bubble_type(self, bubble_type):
			self.paras["bubble_type"] = bubble_type


		@property
		def bubble_style(self):
			return self.paras["bubble_style"]

		@bubble_style.setter
		def bubble_style(self, bubble_style):
			self.paras["bubble_style"] = bubble_style


		@property
		def is_necessary(self):
			return self.paras["is_necessary"]

		@is_necessary.setter
		def is_necessary(self, is_necessary):
			self.paras["is_necessary"] = is_necessary


		@property
		def is_changeable(self):
			return self.paras["is_changeable"]

		@is_changeable.setter
		def is_changeable(self, is_changeable):
			self.paras["is_changeable"] = is_changeable


		@property
		def c_float_range(self):
			return self.paras["c_float_range"]

		@c_float_range.setter
		def c_float_range(self, c_float_range):
			self.paras["c_float_range"] = c_float_range


		@property
		def a_float_range(self):
			return self.paras["a_float_range"]

		@a_float_range.setter
		def a_float_range(self, a_float_range):
			self.paras["a_float_range"] = a_float_range


		@property
		def cost_per_square(self):
			return self.paras["cost_per_square"]

		@cost_per_square.setter
		def cost_per_square(self, cost_per_square):
			self.paras["cost_per_square"] = cost_per_square


		@property
		def area(self):
			return self.paras["area"]

		@area.setter
		def area(self, area):
			self.paras["area"] = area


		@property
		def cost(self):
			return self.paras["cost"]

		@cost.setter
		def cost(self, cost):
			self.paras["cost"] = cost


		@property
		def geos(self):
			return self.paras["geos"]

		@geos.setter
		def geos(self, geos):
			self.paras["geos"] = geos


