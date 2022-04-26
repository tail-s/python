# # file = open("my_file.txt")
#
# with open("my_file.txt") as file: # with으로 열면 안닫아도 됨.
#     contents = file.read()
#     print(contents)
#     # file.close() # 파일을 열면 자원을 차지하게 되는데 그 리소스를 해방시키는 것.

with open("my_file.txt", mode="a") as file: # mode = r / w / a ...
    file.write("\nNew text.")
