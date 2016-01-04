def func(a,b,c=9,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

func(1,2,*[1,2],**{'x':5,'y':9})


