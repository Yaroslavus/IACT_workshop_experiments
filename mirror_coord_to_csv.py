import numpy, pandas

mirror_coordinates_from_KB = {}

mirror_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])

x0, x1, x2, x3 = 0, 536.9355, 1073.871, 1610.807
mirror_x = np.array([x0, x1, x1, x0, -x1, -x1, x0, x1, x2, x2, x2, x1, 0, -x1, -x2, -x2, -x2, -x1, x0, x1, x2, x3, x3, x3, x3, x2, x1, x0, -x1, -x2, -x3, -x3, -x3, -x3, -x2, -x1])

y0, y1, y2, y3, y4, y5, y6 = 0, 310, 620, 930, 1240, 1550, 1860
mirror_y = np.array([y2, y1, -y1, -y2, -y1, y1, y4, y3, y2, y0, -y2, -y3, -y4, -y3, -y2, y0, y2, y3, y6, y5, y4, y3, y1, -y1, -y3, -y4, -y5, -y6, -y5, -y4, -y3, -y1, y1, y3, y4, y5])

z0, z1, z2, z3, z4 = 40.673, 164.708, 122.982, 379.314, 296.896 
mirror_z = np.array([z0, z0, z0, z0, z0, z0, z1, z2, z1, z2, z1, z2, z1, z2, z1, z2, z1, z2, z3, z4, z4, z3, z4, z4, z3, z4, z4, z3, z4, z4, z3, z4, z4, z3, z4, z4])

mirror_alpha = np.array([3.750004, 1.872489, 1.872489, 3.750004, 1.872489, 1.872489, 7.5625, 5.64723, 3.760468, 0, 3.760468, 5.64723, 7.5625, 5.64723, 3.760468, 0, 3.760468, 5.64723, 11.52026, 9.535288, 7.595914, 5.686597, 1.885899, 1.885899, 5.686597, 7.595914, 9.535288, 11.52026, 9.535288, 7.595914, 5.686597, 1.885899, 1.885899, 5.686597, 7.595914, 9.535288])

mirror_beta = np.array([0, 3.249625, 3.249625, 0, -3.249625, -3.249625, 0, 3.283781, 6.565772, 6.565772, 6.565772, 3.283781, 0, 3.283781, 6.565772, 6.565772, 6.565772, 3.283781, 0, 3.36273, 6.68509, 10.03559, 9.929937, 9.929937, 10.03559, 6.68509, 3.36273, 0, 3.36273, 6.68509, 10.03559, 9.929937, 9.929937, 10.03559, 6.68509, 3.36273])

mirror_coordinates_from_KB["mirror_numbers"] = mirror_numbers
mirror_coordinates_from_KB["mirror_x"] = mirror_x
mirror_coordinates_from_KB["mirror_y"] = mirror_y
mirror_coordinates_from_KB["mirror_z"] = mirror_z
mirror_coordinates_from_KB["mirror_alpha"] = mirror_alpha
mirror_coordinates_from_KB["mirror_beta"] = mirror_beta

pd_mirror_coordinates_from_KB = pd.DataFrame(mirror_coordinates_from_KB)

print(pd_mirror_coordinates_from_KB)
pd_mirror_coordinates_from_KB.to_csv(r'/home/yaroslav/IACT_calculations_and_tests/Mirror_coordinates_and_angles_from_KB.csv', header=None, index=None, sep=' ', mode='a')