def transform_data(sales, customers, products):
    sales = sales.dropna()
    # merged = sales.merge(customers, on='ID', how='left')
    # merged = merged.merge(products, on='CustomerID', how='left')
    
    # Unimos customers con products usando:
    # - left_on: 'ID' (columna en customers)
    # - right_on: 'CustomerID' (columna en products)
    merged = customers.merge(
        products,
        left_on='ID',          # Columna en customers
        right_on='CustomerID', # Columna en products
        how='left'             # Left join para mantener todos los clientes
    )
    return merged

