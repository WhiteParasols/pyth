name='Alice'
print(name)
print('hello',name) #argument로 받으면 띄어쓰기 자동
print('hello'+ name) #덧셈 연산은 띄어쓰기 안해줌
print(name)

name1='bob'
name2='charlie'
print('hello, {}'.format(name))
print('hello, {}! {}'.format(name2,name1))
print('hello, {1}! {0}'.format(name2,name1))

#f-string
print(f'hello, {name}')