class mirror:

#number_kb - номер зеркала по версии чертежей КБ
#x_kb, y_kb, z_kb - координаты зеркал по версии чертежей КБ относительно нулевого зеркала
#alpha_YZ_kb, beta_XZ_kb - углы наклонов зеркал по версии КБ. Углы заданы в указанных плоскостях.
#x_dev_exp, y_dev_exp - координаты отражений точечного источника от зеркал на плоскости, расположенной в фокусе телескопа
#f_kb - Фокус телескопа по версии КБ
#f_exp - измеренное с помощью лазерного дальномера расстояние от кольца телескопа до ПЛОЩАДОК под зеркала (зеркала = площадки + 130 мм)
#fix_angle_deg - максимальных угол, на который можно отъюстировать зеркало (приблизительное значение). В градусах.
#z_df_kb - расстояние от зеркала до плоскости, проходящей через двойной фокус телескопа и перпендикулярной его фокусу, рассчитанное исходя из x_kb, y_kb, z_kb
#z_df_exp - расстояние от зеркала до плоскости, проходящей через двойной фокус телескопа и перпендикулярной его фокусу, рассчитанное исходя из x_, y_kb, z_kb

	def __init__(self, number_kb, x_kb, y_kb, z_kb, alpha_YZ_kb, beta_XZ_kb, x_dev_exp, y_dev_exp, f_exp, f_kb=475, fix_angle_deg=5):

		self.number_kb = number_kb
		self.x_kb = x_kb
		self.y_kb = y_kb
		self.z_kb = z_kb
		self.alpha_YZ_kb = alpha_YZ_kb
		self.beta_XZ_kb = beta_XZ_kb
		self.x_dev_exp = x_dev_exp
		self.y_dev_exp = y_dev_exp
		self.f_kb = f_kb
		self.f_exp = f_exp
		self.fix_angle_deg = fix_angle_deg

