goods = [
   {"title": "Ковер", "color": "green", "amount": 256},
   {"title": "Диван для отдыха", "price": 5300, "color": "black", "amount":102},
   {"title": "Картина", "price": 3120, "color": "white", "amount": 53},
   {"title": "Лампа", "price": 550, "color": "blue", "amount": 96},
]

def field(items, *args):
    assert len(args) > 0
    r = [{} for i in range(len(items))]
    for i in range(len(items)):
        for key in items[i]:
            if key in args:
                r[i].update({key:items[i][key]})
                
    return r

if __name__=="__main__":
  for g in field(goods, "title", "price", "amount"):
      print(g)