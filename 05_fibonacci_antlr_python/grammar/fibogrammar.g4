grammar Fibo;

prog
  : expr EOF
  ;

expr
  : FIBO '(' INT ')'
  ;

FIBO: 'FIBO';
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;

