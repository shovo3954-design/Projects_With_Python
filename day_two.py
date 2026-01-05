import numpy as np

python_list = [1,2,3,4,5,6,7,8,9]
print(python_list)

Numpy_array = np.array(python_list) #one
print(Numpy_array)


array_2d = np.array([[3,4,5,6],
                    [3,4,5,6]]) #two

print(array_2d)


mixed_array = np.ones((3,4)) #three
print (mixed_array )

filled_array = np.full((2,2), 5) #four
print(filled_array)

arrange = np.arange(1,300, 4) #five
print(arrange)

identity_matrix = np.eye(4) #six
print(identity_matrix)

array_shape = np.array([[1,2,3], [2,3,4]]) #seven
print (array_2d.shape)

array_size = np.array([[34,5,3,2,4], [3,5,3,6,2]]) #eight
print(array_size.size) # Size function is used to know the size of the element.

arr_1d = np.array([1,2,3]) # nine
arr_2d = np.array([[1,2,3],[3,5,6]])
arr_3d = np.array([[[1,2], [4,5], [4,2], [4,2]]])
print(arr_1d.ndim) # In order to know the dimension of an array
print(arr_2d.ndim)
print(arr_3d.ndim)

arr_type = np.array([4.4, 2.4, 5.2]) # ten
print(arr_type.dtype) # Finding the array type.

arr_change = arr_type.astype(int) #eleven
print(arr_change.dtype)

# Day three
# Mathmetical operation.

arra = np.array([3,3,2,6,3,2,6,6])
print(arra + 5)
print(arra - 5)
print(arra * 5)
print(arra / 5)
print(arra % 5)
print(arra ** 5)


