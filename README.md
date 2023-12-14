# Norma Machine
Simulate a register machine functions

## How to use
There's a few .txt files that indicates the mathematical operations as : <br> 
* fatorial.txt [fatorial] <br>
* multiplicacao.txt [multiplication]<br>
* soma.txt [sum].

Inside the .txt files there's the machine behaviour with the following fields pattern exemple:

1: ZER A 2 3 <br>
2: ADD A 30 30  <br>
3: ZER A 7 4  <br>
4: ADD B 5 5  <br>

**Pattern of text input**

*number_of_line:* | Operation(&nbsp;*ZER, ADD or SUB*&nbsp;)&nbsp; | *machine_name* &nbsp;| if positive move to line (*line*)&nbsp;| if negative move to line (*line*)
