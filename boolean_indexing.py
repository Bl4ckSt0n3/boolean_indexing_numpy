import numpy as np

def indexing_op():

	arr = np.arange(24).reshape(6,4)
	array_A = np.array([True, False, True, False])
	array_B = np.array([False, True, True, False, False, True])
	
	print("first arr\n\n", arr, "\n\n\n")
	
	print("arr[:, array_A]\n\n", arr[:, array_A], "\n\n\n")
	print("arr[array_B, :]\n\n", arr[array_B, :], "\n\n\n")

	ar = arr > 12
	
	print("ar\n\n", ar,"\n\n")
	print("arr[ar]\n\n", arr[ar], "\n\n\n")
	
	
	arr[ar] = -1
	print("arr[ar]=-1\n\n", arr, "\n\n\n")

	
	
if __name__ == "__main__":

	indexing_op()	
	
	

	
