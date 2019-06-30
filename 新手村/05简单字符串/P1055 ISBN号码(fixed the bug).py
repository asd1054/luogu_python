# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-06-09 20:15:03
'''
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


# 做修改 将replace的部分 直接字符串拼接， 全过
numstr = input()
num = numstr[0]+numstr[2:5]+numstr[6:11]+numstr[12]
sum = 0
for i in range(9):
    sum += int(num[i])*(i+1)
pd = sum%11
if pd == 10:
    pd = 'X'
else:
    pd = str(pd)
if pd == num[-1]:
    print("Right")
else:
    s =num[0]+'-'+num[1:4]+'-'+num[4:9]+'-'+pd
    print(s)


# 下面给出其他语言的代码

''' 这是以前用c++时写的记录，emmm 看不太懂了， 将就一下吧
#include <iostream>
using namespace std;
int mark[10];
int main() {
    int a, b, c;
    char d;
    int d1;
    cin >> a >> b >> c >> d>>d ;
    b = -b, c = -c;
    if (d == 'X')
        d1 = 10;
    else
        d1 = d - '0';
    int e=b, f=c;
    int sum=a*1;
    int pd ;
    int q[4], w[6];
    
    for (int i = 3; i >0; i--) {
        q[i] =  e % 10;
        e  /= 10;
        sum += q[i] * (i+1);
    }
    for (int i = 6; i >0; i--) {
        w[i] = f % 10;
        f /= 10;
        sum += w[i] * (i + 3);
    }
    pd = sum % 11;
    if (pd == d1) {
        cout << "Right"<<endl;
    }
    else if(pd==10)
        cout << a << "-" << b << "-" << c << "-X" << endl;
    else 
        cout << a<<"-"<<b<<"-"<<c<<"-"<<pd << endl;
    return 0;
}
'''