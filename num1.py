import sys

one = sys.argv[1];
two = sys.argv[2];
operation = sys.argv[3];

print(operation);

if(operation == 1):
  sum= one + two;
  print("Number operation SUM : "+sum);
     
elif(operation == 2):
  sum = one * two;
  print(" Number operation MUL: ",sum); 
            

elif(operation == 3):
  sum = one - two;
  print(" Number operation SUB: ",sum); 
            
       
elif(operation == 4):
  sum = one / two;
  print(" Number operation DIV: ",sum); 
            

