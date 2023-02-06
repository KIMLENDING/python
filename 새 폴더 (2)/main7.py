# f = open('c:/Users/gotsl/Desktop/새 폴더 (2)/abc.txt', 'w')
# for i in range(1, 8):
#     f.write('%d번째\n' % i)
# f.close()

f = open('c:/Users/gotsl/Desktop/새 폴더 (2)/abc.txt', 'r')
m = f.readlines()  # 파일 안에 있는 내용을 읽어서 리스트 형태로 반환
f.close()
# print(m)
for i in m:
    print(i, end='')
