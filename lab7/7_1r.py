def create_n_dim_array_recursive(dimensions, size):
    if dimensions == 1:
        return ['level ' + str(dimensions)] * size
    else:
        return [create_n_dim_array_recursive(dimensions - 1, size) for _ in range(size)]

print(create_n_dim_array_recursive(3, 2))