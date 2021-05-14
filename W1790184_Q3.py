# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: ……2019732………………..…

# Date: ……4/17/2020………………..… 


creditrange = [0,20,40,60,80,100,120]
progress=0
trailing=0
retriever=0
excluded=0

entry=input('click anything to continue, click q to quit:')

while entry !='q':
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
                progress = progress + 1
            elif passcred == 100:
                print("Progress-module trailer")                    #prompting userto enter progress-module retriever  if marks are 100
                trailing = trailing + 1
            elif passcred== 80:
                print(" Do not progress-module retriever")          #prompting user to enter do not progress-module retriever if marks are 80
                retriever = retriever + 1
            elif passcred ==60:
                print("Do not progress-module retriever")           #prompting user to enter do not progress module retriever if marks are 60
                retriever = retriever + 1
            elif passcred ==40:
                if failcred == 80:
                    print("Exclude")
                    excluded = excluded + 1
                else:
                    print("Do not progress-module retriever")       #promting user to enter Do not progress-module retriever 
                    retriever = retriever + 1 

            elif passcred==20:
                if failcred==80:
                    print("exclude")
                    excluded = excluded + 1
        
                elif failcred==100:
                    print("exclude")
                    excluded = excluded + 1
                else:
                    print("Do not progress-module retriever")      #prompt user to enter do not progress-module retriever
                    retriever = retriever + 1    
            elif passcred==0:
                if failcred==80:
                    print("exclude")
                    excluded = excluded + 1
                elif failcred==100:
                    print("exclude")
                    excluded = excluded + 1
                elif failcred==120:
                    print("exclude")
                    excluded = excluded + 1
                else:
                    print("Do not progress-module retriever")
                    retriever = retriever + 1

            entry=input('click anything to continue, click q to quit: ')
                            
    except:
            print("Integers required")      #promting user to enter intigers required when when wrong data is entered 


print("progress",progress,":",progress*"*")
print("trailing",trailing,":",trailing*"*")
print("module retriever",retriever,":",retriever*"*")
print("excluded",excluded,":",excluded*"*")
print(progress+trailing+retriever+excluded,"outcomes in total.")

count = 0
greatestnum = max(progress, trailing, retriever, excluded)         #prompting the user a vertical histogram
print('Progress  Trailing  Retriever  Excluded')
while count <= greatestnum  :
    if progress != 0:
        print('   *         ',end='')
        progress -= 1
    else:
        print('             ', end='')

    if trailing != 0:
        print('*           ',end='')
        trailing -= 1
    else:
        print('            ', end='')

    if retriever != 0:
        print('*          ',end='')
        retriever -= 1
    else:
        print('           ', end='')

    if excluded != 0:
        print('*')
        excluded -= 1
    else:
        print('')
    
    count = count + 1
