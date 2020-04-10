# Коллоквиум

Дискретная математика, 2020 г.
Группа 9307.


Ссылка на задание: https://docs.google.com/document/d/1Dv_6AIhxg_3ezu6VMcEnMpyfRzgym9l8PmE4ULGfjgM/edit .


## Список классов и действий с ними:
\<class\>():
	var1; var2; ...
* Индекс; Кодовое описание; Предполагаемые действия;
* Имя автора.


N():
	list digits[] (int);

* N1	comp_N_N	overload <, >, ==, >=, <=, !=
* Михаил
* N2	!zer_N		overload !=, ==
* Михаил
* N3	inc_N		overload +
* Михаил
* N4	add_N_N		overload +
* Михаил, Ярослав (+)
* N5	sub_N_N		overload -
* Михаил
* N6	mul_N_digit	overload \*
* Дмитрий
* N7	mul_N_10^k	overload \*, \*\*
* Дмитрий
* N8	mul_N_N		overload \*
* Дмитрий
* N9	(== N5 + N6)
* Дмитрий
* N10	(== N11 с ограничениями? Не понял, зачем вообще нужен этот пункт)
* Дмитрий
* N11	div_N_N		overload //
* Илья
* N12	mod_N_N		overload %
* Илья
* N13	GCF_N		N = GCF( N1, N2, ... )
* Владимир
* N14	LCM_N		N = LCM( N1, N2, ... )
* Владимир


Z():
	bool sign;
	list digits[] (int);

* Z1	abs_Z		overload abs()
* Екатерина
* Z2	comp_Z_0	overload <, >, ==, >=, <=, !=
* Екатерина, Ярослав (-?)
* Z3	mul_Z_-1	overload \*
* Екатерина
* Z4	trans_N->Z	Z = N.toZ()
* Екатерина
* Z5	trans_Z->N	N = Z.toN()
* Екатерина
* Z6	add_Z_Z		overload +, use N::(+) with sign check.
* Яна
* Z7	sub_Z_Z		overload -, use N::(+), N::(-) with sign check.
* Яна
* Z8	mul_Z_Z		overload \*, use N::(\*) with sign check.
* Яна
* Z9	div_Z_Z		overload //, use N::(//)
* Яна
* Z10	mod_Z_Z		overload %, use N::(%)
* Яна


Q():
	Z num;
	N denum;

* Q1	reduce_Q	Q = Q.reduce()
* Максим
* Q2	isint_Q		bool = Q.isInt()
* Максим
* Q3	trans_Z_Q	Q = Z.toQ()
* Максим
* Q4	trans_Q_Z	Z = Q.toZ()
* Максим
* Q5	add_Q_Q		overload +, use Z::(+)
* Максим
* Q6	sub_Q_Q		overload -, use Z::(-)
* Максим
* Q7	mul_Q_Q		overload \*, use Z::(\*)
* Максим
* Q8	div_Q_Q		overload /, use Z::(\*)
* Максим


P():
	list coef[] (Q);

* P1	add_P_P		overload +
* --
* P2	sub_P_P		overload -
* --
* P3	mul_P_Q		overload \*
* --
* P4	mul_P_x^k	overload \*
* --
* P5	leadcoef_P	Q = P.leadcoef()
* --
* P6	deg_P		N = P.deg()
* -
* P7	factor_P	?
* Илья
* P8	mul_P_P		overload \*
* Илья
* P9	div_P_P		overload //
* Илья
* P10	mod_P_P		overload %
* Полина (+-)
* P11	GCF_P		? = GCF( P1, P2, ... )
* Никита (+?)
* P12	dervtive_P	P = P.derivative()
* Никита (+?)
* P13	nmr_P		P = P.nmr()
* Полина (+-)
