数据结构,特点,增加 (Add),删除 (Delete),修改 (Update),查询 (Search)
List (列表),有序、可重复,"append() (末尾)insert(i, x) (指定位置)",pop(i) (按索引)remove(x) (按值),list[i] = x,list[i] (索引)in (判断存在)
Set (集合),无序、唯一,add(),remove(x)discard(x) (删不存在的不会报错),不支持索引修改(通常是先删再加),in (极快 O(1))
Dict (字典),键值对、键唯一,d[key] = value,pop(key)del d[key],d[key] = new_value,"d[key]d.get(key, default)"
Tuple (元组),不可变,不支持,不支持,不支持,tuple[i]
