# infa12

**30 ПАРАГРАФ**

**ВОПРОСЫ**
1) Перед сложением или вычитанием вещественных чисел требуется выравнивать порядки, потому что значащие части чисел должны быть выражены в одинаковой степени, чтобы их можно было корректно сложить или вычесть. Без выравнивания порядков результат будет некорректным из-за сдвига значащих цифр.
2) При выравнивании порядков сдвигу подвергается число с меньшим порядком, потому что его значащую часть необходимо подогнать к значащей части числа с большим порядком. Это позволяет выполнить корректное сложение или вычитание чисел.
3) Да, при выравнивании порядков значащая часть всегда сдвигается вправо, чтобы уменьшить её порядок и подогнать к значащей части числа с большим порядком. Это обеспечивает правильное сложение или вычитание.
4) Количество сдвигов можно вычислить как разность порядков двух чисел. Если разность равна n, то значащую часть числа с меньшим порядком нужно сдвинуть вправо на n разрядов.
5) Да, при сложении вещественных чисел может возникнуть ситуация, когда значащие части придётся вычитать, если числа имеют противоположные знаки. В этом случае операция сводится к вычитанию меньшего числа из большего.
6) Если умножить вещественное число на 2, его двоичный код сдвинется на один разряд влево, увеличивая порядок на единицу. Для целого числа при удвоении также происходит сдвиг на один разряд влево, увеличивая значение числа в два раза.
7) Такие случаи возможны, когда разность порядков чисел A и B настолько велика, что значащая часть числа B становится несущественной и отбрасывается при выравнивании порядков. Это происходит, если разность порядков превышает количество разрядов значащей части.
8) Переполнение при вычитании возможно, если результат выходит за пределы диапазона представления чисел. Антипереполнение может произойти, если результат слишком мал и становится равным нулю, что также вызывает потерю точности.
9) При умножении вещественных чисел их значащие части перемножаются, а порядки складываются. При делении значащие части делятся, а порядки вычитаются. После выполнения операции результат нормализуется, если это необходимо.
10) Да, это верно. Переполнение возникает, когда результат умножения не помещается в отведённое количество разрядов значащей части. В этом случае старшие разряды теряются, что приводит к некорректному результату.
11) Да, в результате арифметической операции нормализация может нарушиться, если значащая часть результата выходит за пределы допустимого диапазона. В таких случаях необходимо нормализовать результат, сдвинув значащую часть и изменив порядок.

**ЗАДАЧИ**
1) Порядки выравниваются до большего, число 1,11·2^11 будет сдвинуто на 1 разряд. 
2) Число 2,625 в формате single: 40 28 00 00^16. 
3) Число –2,375 в формате single: C0 18 00 00^16. 
4) 0,110 =  0,0(0011)2, т.е. в заданной разрядности с округлением последнего бита  
1,1001101·2^–100 
; 0,2 вдвое больше, поэтому достаточно у предыдущего числа к порядку  
прибавить единицу: 1,1001101·2^–11. С учетом округления сумма будет равна   
1,0011010·2^–10. 
5) – 
6)  Разница порядков у   с любым из оставшихся чисел равна   
111 – (–10) = 1001^2 = 9. 
Это означает, что при выравнивании порядков значащая часть чисел B, C, D или E заведомо  
«покинет» 8‐разрядную сетку. Следовательно, A+B+C+D+E = A. Теперь просуммируем в об‐ 
ратном порядке. Сумму четырех одинаковых слагаемых легко найти, если вспомнить, что  
каждое умножение на 2 – это увеличение порядка на 1. В итоге   
E+D+C+B = 4⋅B = 1,0⋅2^–10+10 = 1,0⋅2^0 
. 
Поскольку теперь разность порядков уже меньше разрядности значащей части, то получим  
другой ответ: 1,0000001⋅2^111. Эффект можно объяснить так. Каждое из чисел B, C, D или E 
мало по сравнению с A и поэтому при сложении с ним просто теряется. Тем не менее, если  
все их предварительно сложить, то сумма уже попадет на разрядную сетку и даст неболь‐ 
шую добавку к значению A. 
7) 1,111·2^‐1 
8) 1,001·2^10001, произойдет переполнение.
9) 1,1·21   
10) Получится 1,1·2^‐10001, порядок не поместится в 4‐битную область

**31 ПАРАГРАФ**

**ВОПРОСЫ**

