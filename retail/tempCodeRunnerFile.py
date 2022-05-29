).where('material_catalog','array_contains', material_name).get()
    lis  =  doc.to_dict()