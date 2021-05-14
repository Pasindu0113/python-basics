progress=0
trailing=0
retriever=0
excluded=0

passcred = [120, 100, 100, 80, 60, 40, 20, 20, 20, 0]
defercred = [0, 20, 0, 20, 40, 40, 40, 20, 0, 0]
failcred = [0, 0, 20, 20, 20, 40, 60, 80, 100, 120]
for i in range(0,10):
            if passcred[i]==120:
                print("progress")                             #promting user to enter progress if marks are 120
                progress = progress + 1
            elif passcred[i] == 100:
                print("Progress-module trailer")                    #prompting userto enter progress-module retriever  if marks are 100
                trailing = trailing + 1
            elif passcred[i]== 80:
                print("Do not progress-module retriever")          #prompting user to enter do not progress-module retriever if marks are 80
                retriever = retriever + 1
            elif passcred[i] ==60:
                print("Do not progress-module retriever")           #prompting user to enter do not progress module retriever if marks are 60
                retriever = retriever + 1
            elif passcred[i] ==40:
                if failcred[i] == 80:
                    print("Exclude")
                    excluded = excluded + 1
                else:
                    print("Do not progress-module retriever")       #promting user to enter Do not progress-module retriever 
                    retriever = retriever + 1 

            elif passcred[i]==20:
                if failcred[i]==80:
                    print("exclude")
                    excluded = excluded + 1
        
                elif failcred[i]==100:
                    print("exclude")
                    excluded = excluded + 1
                else:
                    print("Do not progress-module retriever")      #prompt user to enter do not progress-module retriever
                    retriever = retriever + 1    
            elif passcred[i]==0:
                if failcred[i]==80:
                    print("exclude")
                    excluded = excluded + 1
                elif failcred[i]==100:
                    print("exclude")
                    excluded = excluded + 1
                elif failcred[i]==120:
                    print("exclude")
                    excluded = excluded + 1
                else:
                    print("Do not progress-module retriever")
                    retriever = retriever + 1

        

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
