print("Welcome to the Quiz! \n Answer the following questions\n-----------------------------------------------------------")
l =[['What is the capital of France?',['Paris','London','Berlin','Madrid','Enter your answer (1/2/3/4):']],
    ['Who wrote Harry Potter series of books?',['J.K. Rowling','Stephen King','George R.R. Martin','J.R.R. Tolkien','Enter your answer (1/2/3/4):']],
    ['What is the largest planet in our solar system?',['Earth','Mars','Jupiter','Saturn','Enter your answer (1/2/3/4):']
     ]]
z= 0
for i,v in enumerate(l):
    print(i+1,v[0])
    for x,y in enumerate(v[1]):
        '''ques = f"{i+1}. {y}"'''
        print(x+1,y)
        if y == "Enter your answer (1/2/3/4):":
            n = int(input())
            if n == 1 and 3:
                print("correct")
            else:
                print('wrong')
        
            

    
        


        

        
        

    
    '''for key, data in enumerate(v):
        ques = f"{i+1}. {data}"
        print(key, data)
        print('------')'''
#         if x == '4. Madrid':
#             n = int(input("Enter your answer (1/2/3/4):  "))
#             if n == 1:
#                 print("correct")
#                 z=+1
#             else:
#                 print("wrong")
#         if x == '4. J.R.R. Tolkien':
#             n = int(input("Enter your answer (1/2/3/4): "))
#             if n == 1:
#                 print("correct")
#                 z= z+1
#             else:
#                 print("wrong") 
#         if x == '4. Saturn':
#             n = int(input("Enter your answer (1/2/3/4): "))
#             if n == 3:
#                 print("correct")
#                 z= z+1
#             else:
#                 print("wrong") 

# print(f"You answered {z} out of 3 questions correctly.")
        
