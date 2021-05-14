# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: ……2019732………………..…

# Date: ……4/17/2020………………..… 

creditrange = [0,20,40,60,80,100,120]

try:
    passcred = int(input("Enter the pass credits: "))             #prompting user to enter the pass credit marks
    defercred = int(input("Enter the defer credits: "))           #promting user to enter the difered credit marks
    failcred = int(input("Enter the fail credits: "))             #promting user to enter the fail credit marks 

    usercredlist = [passcred,defercred,failcred]                #promting the use to enter range error if invalid value is entered 
    for i in range(3):
        if usercredlist[i] not in creditrange:
            print('Range error')
            break

    total=120
    if total!=(passcred+defercred+failcred):                    
          print("total incorrect")

    else:
            if passcred==120:
                print("progress")                             #promting user to enter progress if marks are 120
            elif passcred == 100:
                print("Progress-module trailer")                    #prompting userto enter progress-module retriever  if marks are 100
            elif passcred== 80:
                print(" Do not progress-module retriever")          #prompting user to enter do not progress-module retriever if marks are 80
            elif passcred ==60:
                print("Do not progress-module retriever")           #prompting user to enter do not progress module retriever if marks are 60
            elif passcred ==40:
                if failcred == 80:
                    print("Exclude")
                else:
                    print("Do not progress-module retriever")       #promting user to enter Do not progress-module retriever 
                   
            elif passcred==20:
                if failcred==80:
                    print("exclude")
                elif failcred==100:
                    print("exclude")
                else:
                    print("Do not progress-module retriever")      #prompt user to enter do not progress-module retriever
                       
            elif passcred==0:
                if failcred==80:
                    print("exclude")
                elif failcred==100:
                    print("exclude")
                elif failcred==120:
                    print("exclude")
                else:
                    print("Do not progress-module retriever")
                    
except:
    print("Integers required")
    
       
