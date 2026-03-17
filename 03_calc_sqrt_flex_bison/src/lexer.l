%option noyywrap

%{
  #include "parser.tab.h"
  #include <stdlib.h>
%}

DIGIT      [0-9]
INT        {DIGIT}+
FRAC       ({DIGIT}*"."{DIGIT}+)|({DIGIT}+"."{DIGIT}*)
NUMBER     ({FRAC}|{INT})
WS         [ \t\r]+

%%

{WS}                ;

"sqrt"              return SQRT;

{NUMBER}            { yylval.num = strtod(yytext, NULL); return NUMBER; }

"\n"                return EOL;

"+"                 return '+';
"-"                 return '-';
"*"                 return '*';
"/"                 return '/';
"("                 return '(';
")"                 return ')';

.                   return INVALID;

%%
