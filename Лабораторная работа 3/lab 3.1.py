def find_first_index(products, item):
    for index, current_item in enumerate(products):
        if current_item == item:
            return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list,find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
