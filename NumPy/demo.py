import numpy as np

# list = [1,2,3,4,5]

# arr_list = np.array(list)
# print(arr_list)


# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# arr1 = np.array([list1, list2])
# print(arr1)


# print(arr1.ndim)  #---->>gives number of dimensions
# print(arr1.shape)  #---->>gives shape of array
# print(arr1.size)  #---->>gives size of array
# print(arr1.dtype)  #---->>gives data type of array



# methods of numpy
# zero array

# arr = np.zeros((3,4))
# print(arr)    

# one array
# arr1 = np.ones((3,4))
# print(arr1)

# full array
# arr2 = np.full((3,4), 5)
# print(arr2)

# identity matrix
# arr = np.eye(3 )
# print(arr)

# empty array
# arr = np.empty((3,4))
# print(arr)

# evenly spaced array
# arr = np.arange(1,10,3)
# print(arr)

# specific values between a range
# arr = np.linspace(1,10,5)
# print(arr)  #equaliy spaced 5 values between 1 and 10


# random values
# arr = np.random.rand(3,4)
# print(arr)  #---->>gives random values between 0 and 1    --->float format

#random integer values
# arr = np.random.randint(1,10, size=(3,4))
# print(arr)  #---->>gives random integer values between 1 and 10


# array ondexing and slicing
# arr = np.array([[1,2,3,4,5],
#                 [6,7,8,9,10],
#                 [11,12,13,14,15]])      
# print(arr[1,2])  #---->>gives value at 1st row and 2nd column


# array reshaping and flattening 
# arr = np.array([[1,2,3,4,5],
#                 [6,7,8,9,10],
#                 [11,12,13,14,15]])
# print(arr.reshape(5,3))  #---->>reshaping array to 5 rows and 3 columns
# print(arr.flatten())  #---->>flattening array to 1D array


# array stacking and splitting
# arr1 = np.array([[1,2,3],
#                  [4,5,6]])
# arr2 = np.array([[7,8,9],
#                  [10,11,12]])
# # print(np.vstack((arr1, arr2)))  #---->>vertical stacking of two arrays
# # print(np.hstack((arr1, arr2)))  #---->>horizontal stacking

# print(np.hsplit(arr1, 2, axis=1))  #---->>splitting array into 2 parts along columns



#mathematical operations
# arr1 = np.array([[1,2,3],
#                  [4,5,6]])
# arr2 = np.array([[7,8,9],
#                  [10,11,12]])     
# print(np.add(arr1, arr2))  #---->>addition of two arrays
# print(np.subtract(arr1, arr2))  #---->>subtraction of two arrays
# print(np.multiply(arr1, arr2))  #---->>multiplication of two arrays
# print(np.divide(arr1, arr2))  #---->>division of two arrays
# print(np.dot(arr1, arr2.T))  #---->>dot product of two arrays
# print(np.transpose(arr1))  #---->>transpose of array



#broadcasting
# arr1 = np.array([[1,2,3],
#                  [4,5,6]])
# arr2 = np.array([1,2,3])
# print(arr1 + arr2)  #---->>broadcasting of arr2 to arr1 and then addition of two arrays 


#nan and inf values
# arr = np.array([1,2,np.nan,4,np.inf])
# print(np.isnan(arr))  #---->>check for nan values
# print(np.isinf(arr))  #---->>check for inf values 
# print(np.nan_to_num(arr))  #---->>replace nan and inf values with 0


#save and load array
arr = np.array([[1,2,3],
                 [4,5,6]])
np.save('array.npy', arr)  #---->>save array to file
loaded_arr = np.load('array.npy')  #---->>load array from file
print(loaded_arr)