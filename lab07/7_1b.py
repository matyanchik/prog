def create_n_dim_array(dimensions, size):
    array = []
    for _ in range(size):
        array.append('level ' + str(dimensions))
    
    for _ in range(dimensions - 1):
        array = [array.copy() for _ in range(size)]
    
    return array

print(create_n_dim_array(3, 2))