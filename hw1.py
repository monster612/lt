def foo(a,b,*c,d,e,**f):
	print(a,b,c,d,e,f,sep='\n')
print(foo(1,2,3,4,5,d=6,e=7,f=8,g=9))