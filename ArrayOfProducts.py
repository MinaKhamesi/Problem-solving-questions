def arrayOfProducts(array):
    products_coming_from_left = [1]
	for i in range(len(array)-1):
		products_coming_from_left.append(products_coming_from_left[-1]*array[i])
		
	products_coming_from_right = [1]
	for i in reversed(range(1,len(array))):
		products_coming_from_right.append(products_coming_from_right[-1]*array[i])
	
	products_coming_from_right.reverse()
	
	productsArray = [1 for num in array]
	for i in range(len(array)):
		productsArray[i] = products_coming_from_right[i] * products_coming_from_left[i]
	
	return productsArray


def arrayOfProducts(array):
    products = [1 for _ in array]
	
	runningProductFromLeft = 1
	for i in range(len(array)):
		products[i] = runningProductFromLeft
		runningProductFromLeft *= array[i]
	
	runningProductFromRight = 1
	for i in reversed(range(len(array))):
		products[i] *= runningProductFromRight
		runningProductFromRight *= array[i]
	
	return products