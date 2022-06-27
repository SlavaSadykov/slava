class SparseArray:
  def __init__(self):
    self.massiv = {}

  def __setitem__(self, key, value):
     self.massiv[key] = value

  def __getitem__(self, key):
     return self.massiv.get(key, 0)

    
arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))
