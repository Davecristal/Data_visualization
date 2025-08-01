import json

# 探索数据的结构
filename = 'study/update_from_net/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'study/update_from_net/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))  # 打印地震数量

mags, titles, lons, lats = [], [], [], [] 
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])  # 打印前10个地震的震级
print(titles[:10])  # 打印前10个地震的标题
print(lons[:10])  # 打印前10个地震的经度
print(lats[:10])  # 打印前10个地震的纬度

