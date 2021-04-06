demo_dict = {'sds':[4,5],
              'is':[6,7],
              'go':[8,9]}
print("dic is : ",demo_dict)
res = dict()
for key in sorted(demo_dict):
    res[key] = sorted(demo_dict[key])
print("sorted dict : ",str(res))