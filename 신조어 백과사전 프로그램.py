inf=[]
mean=[]
while(True):
    print("========신조어 백과사전 프로그램========")
    print("1.단어 등록")
    print("2.단어 검색")
    print("3.단어 삭제")
    dic = int(input("원하는 메뉴를 선택해주세요"))

    if dic==1:
        word= input("등록할 단어를 입력해주세요")
        meaning= input("등록하실 단어의 뜻을 입력해주세요")
        inf.append(word)
        mean.append(meaning)
        print("단어가 등록되었습니다.",end="\n\n")
    elif dic==2:
        word= input("검색할 단어를 입력하세요")
        if word in inf:
            temp=inf.index(word)
            print("{}:{}".format(word,mean[temp]))
            print()
        else:
            print("해당 단어가 등록이 되어 있지 않습니다.")
            print()
    elif dic==3:
        word= input("삭제할 단어를 입력해주세요 ")
        inf.remove(word)
        print("단어가 삭제되었습니다.",end="\n\n")
