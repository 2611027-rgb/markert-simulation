
product = {}

# Mart 클래스
class Mart:
  def __init__(self,b,c):
    self.price = float(b)
    self.amount = int(c)

  # 상품 수량 추가 메서드
  def add_amount(self,d):
    d_int = int(d)
    self.amount += d_int
    return self.amount

# 시작 시 파일에서 상품 목록을 로드
# 파일 형식: 상품명,가격,수량
with open('product.txt', 'r') as f:
  lines = f.readlines()
  for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 3:
      name = parts[0]
      price = float(parts[1])
      amount = int(parts[2])
      product[name] = Mart(price, amount)

# 새 상품 추가 함수
# 상품명, 가격, 수량을 입력
def add_product():
  name_of_product = input('상품명 입력 >>>')
  price_of_product = float(input('상품 가격 입력 >>>')) # 예외 처리 제거
  amount_of_product = int(input('상품 수량 입력 >>>'))   # 예외 처리 제거

  product[name_of_product] = Mart(price_of_product,amount_of_product)

# 메인 프로그램 루프: 사용자 명령을 처리합니다.
print('명령어 종류:[add,save,add_quant,check,reset]')
while True:
  input_content = input('무엇을 할 것인가? >>>')
  # 새 상품을 추가 명령어
  if input_content == 'add':
    add_product()
    # 추가된 상품의 현재 목록 출력 명령어
    for name, item in product.items():
      print(f"상품: {name}, 가격: {item.price}, 수량: {item.amount}")
  # 파일에 저장 명령어
  elif input_content == 'save':
    with open('product.txt', 'w') as f:
      for x,i in product.items():
        f.write(f"{x},{i.price},{i.amount}\n")
    print('저장 완료')
    break
  #상품의 수량 추가 명령어
  elif input_content == 'add_quant':
    a = input('어떤 상품의 수량을 추가할 것인가?>>>')
    if a in product:
      quant = input('vntkhkg >>>')
      new_amount = product[a].add_amount(quant)
      print(f"{a}: {new_amount}")
    else:
      print("상품을 찾을 수 없음.")
  # 현재 재고 목록 확인 명령어
  elif input_content == 'check':
    if product:
      for name, item in product.items():
        print(f"상품: {name}, 가격: {item.price}, 수량: {item.amount}")
    else:
      print("재고가 없음.")
   #재고 전체 삭제 명령어
  elif input_content == 'reset':
    with open('product.txt','w') as f:
      f.write(None)
  # 알 수 없는 명령어
  else:
    print("알 수 없는 명령어")
