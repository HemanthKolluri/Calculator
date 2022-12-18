def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
  
operation={
"+":add,
"-":sub,
"*":multiply,
"/":divide
}
should_continue=True
a=float(input("Enter First Number : "))

while should_continue:
  b=float(input("Enter Next Number : "))
  for i in operation:
    print(i)
  S=input("Select operation : ")
  T=operation[S]
  Total=T(a,b)
  print(f"{a}{S}{b}={Total}")
  if input(f"Type 'Y' to continue calulation with {Total} or 'N'to stop :").lower()=="y":
    a=Total
  else:
    should_continue=False