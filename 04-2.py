class ReversedList:
  def __init__(self, lst):
    self.l = list(reversed(lst))
     
  def __str__(self):
    return str(self.l)
    
  def __getitem__(self, i):
    return self.l[i]
    
  def __len__(self):
    return len(self.l)

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
  print(rl[i])
