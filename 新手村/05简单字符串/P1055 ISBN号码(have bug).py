'''
题目描述
每一本正式出版的图书都有一个ISBN号码与之对应，ISBN码包括99位数字、11位识别码和33位分隔符，其规定格式如x-xxx-xxxxx-x，其中符号-就是分隔符（键盘上的减号），最后一位是识别码，例如0-670-82162-4就是一个标准的ISBN码。ISBN码的首位数字表示书籍的出版语言，例如00代表英语；第一个分隔符-之后的三位数字代表出版社，例如670670代表维京出版社；第二个分隔符后的五位数字代表该书在该出版社的编号；最后一位为识别码。

识别码的计算方法如下：

首位数字乘以11加上次位数字乘以22……以此类推，用所得的结果 \bmod 11mod11，所得的余数即为识别码，如果余数为1010，则识别码为大写字母XX。例如ISBN号码0-670-82162-4中的识别码44是这样得到的：对067082162这99个数字，从左至右，分别乘以1,2,...,91,2,...,9再求和，即0×1+6×2+……+2×9=1580×1+6×2+……+2×9=158，然后取158 \bmod 11158mod11的结果44作为识别码。

你的任务是编写程序判断输入的ISBN号码中识别码是否正确，如果正确，则仅输出Right；如果错误，则输出你认为是正确的ISBN号码。

输入输出格式
输入格式：
一个字符序列，表示一本书的ISBN号码（保证输入符合ISBN号码的格式要求）。

输出格式：
一行，假如输入的ISBN号码的识别码正确，那么输出Right，否则，按照规定的格式，输出正确的ISBN号码（包括分隔符-）。

输入输出样例
输入样例#1： 
0-670-82162-4
输出样例#1： 
Right
输入样例#2： 
0-670-82162-0
输出样例#2： 
0-670-82162-4
'''
# 全错？？
# row = input()
# num = row.replace('-','') #可能是不支持replace（）
# sum = 0
# for i in range(9):
#     sum += int(num[i])*(i+1)
# shibiema = "0123456789X"
# pd = sum%11
# if shibiema[pd] == row[-1]:
#     print("Right")
# else:
#     s =row[0:-1]+shibiema[pd]
#     print(s)


# 才70分？？莫名觉丽。
# num = input().replace('-','')
# sum = 0
# for i in range(9):
#     sum += int(num[i])*(i+1)
# pd = sum%11
# if pd == 10:
#     pd = 'X'
# else:
#     pd = str(pd)
# if pd == num[-1]:
#     print("Right")
# else:
#     s =num[0]+'-'+num[1:4]+'-'+num[4:9]+'-'+pd
#     print(s)


# 翻译的c 语言 一样全错。无语了
# isbn = input()
# k = 0
# h = 0
# for i in range(len(isbn)-1):
#     if isbn[i] != '-':
#         k += 1
#         h += k*(ord(isbn[i])-ord('0'))
# h %= 11
# if h == 10:
#     c = 'X'
# else:
#     c = str(h)
# if c == isbn[12]:
#     print("Right")
# else:
#     isbn = isbn[0:-1] + c  
#     print(isbn)

# 下面给出其他语言的代码
'''
#include <iostream>
#include <cstring>//头文件不解释
using namespace std;
int main()
{
    char s[14],c;
    cin>>s;
    int h=0,k=0;
    for(int i=0;i<11;i++)
    {
        if(s[i]!='-')
        {
            k++;
            h+=k*(s[i]-'0');//-0是为了将字符串变成普通数字
        }
    }
    h%=11;
    if(h==10) c='X';
    else c=h+'0';
    if(c==s[12]) cout<<"Right"<<endl;
    else
    {
        s[12]=c;
        cout<<s;
    }
    return 0;
}
'''