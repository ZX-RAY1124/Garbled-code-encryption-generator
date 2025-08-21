## 乱码加密生成器
一款能将正常文本通过utf-8编码后的十六进制代码进行删改等特定操作，   
并用非utf-8解码并生成乱码的工具。  
乱码下方将会附上密钥 

**使用方法**  
_仅适用utf-8文本_  

[r] 将两个不同的十六进制代码进行替换  
[d] 随机删除一个十六进制代码，并且替换为?  
[s] 将文本格式化并输出至*Output.txt*  
[q] 结束程序

**Example:**  
`utf-8 我喜欢你`  
[r] [r] [d]   
`GBK 鎴戝枩娆�?舰`  
`Shift-JIS ?�大万?ｬ｢�ｽ�`  
`Big5 �����賣�Ｖ?�`
   
*由于考虑到转码会出现数据丢失情况，为降低长文章解码难度，编码后文章下方会有全文修改后的二进制码做比对（记得二进制转十六进制）*
***
## Garbled code encryption generator  
A tool that can perform specific operations such as deletion and modification on the hexadecimal code of normal text encoded in UTF-8, and then generate garbled text by decoding it with non-UTF-8. A key will be attached below the garbled text.  
**Usage method**  
_utf-8 text Only(Chinese or others)_  

[r] Replace two different hexadecimal codes  
[d] Randomly delete a hexadecimal code and replace it with?  
[s] Format the text and Output it to *Output.txt*  
[q] End the program

_ASCII text available(English/Caesar cipher/)_  
[i] Enter the index of the letter  
[s] Format the processed text and Output it to *Output.txt*  

**Example**  
`Some days you bloom,Some days you grow roots.`  
index:10  
`CYWO NKIC IYE LVYYW,CYWO NKIC IYE QBYG BYYDC.`





