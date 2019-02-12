def elevator(left,right,call):
  if call <= 2 and call>= 0:
    if call == left and  call== right:
        print ('right')
    elif call > left and call > right:
        print ('right')
    elif call > left and call < right:
        print ('right')
    else:
      if call == left:
        print ('left')
      elif call == right:
        print ('right')
      
  else:
    print ('Invalid call')
   
elevator(0, 1, -1)
# elevator(0, 1, 1)
# elevator(0, 1, 2)
# elevator(0, 0, 0)
# elevator(0, 2, 1)