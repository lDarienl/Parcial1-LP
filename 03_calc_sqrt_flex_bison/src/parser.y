%{
  #include <stdio.h>
  #include <stdlib.h>
  #include <errno.h>
  #include <string.h>

  extern int yylex(void);
  extern FILE *yyin;
  void yyerror(const char *s);

  static double newton_sqrt(double a);
%}

%union {
  double num;
}

%token <num> NUMBER
%token SQRT
%token EOL
%token INVALID

%type <num> expr

%left '+' '-'
%left '*' '/'
%right UMINUS

%%

input
  : /* empty */
  | input line
  ;

line
  : EOL
  | expr EOL           { printf("%.12g\n", $1); }
  | INVALID EOL        { fprintf(stderr, "Error: caracter inválido\n"); }
  ;

expr
  : NUMBER             { $$ = $1; }
  | expr '+' expr       { $$ = $1 + $3; }
  | expr '-' expr       { $$ = $1 - $3; }
  | expr '*' expr       { $$ = $1 * $3; }
  | expr '/' expr       {
                          if ($3 == 0.0) {
                            fprintf(stderr, "Error: división por cero\n");
                            $$ = 0.0;
                          } else {
                            $$ = $1 / $3;
                          }
                        }
  | '-' expr %prec UMINUS { $$ = -$2; }
  | '(' expr ')'        { $$ = $2; }
  | SQRT '(' expr ')'   {
                          if ($3 < 0.0) {
                            fprintf(stderr, "Error: sqrt de negativo\n");
                            $$ = 0.0;
                          } else {
                            $$ = newton_sqrt($3);
                          }
                        }
  ;

%%

static double newton_sqrt(double a) {
  if (a == 0.0) return 0.0;
  double x = a / 2.0;
  if (x == 0.0) x = 1.0;

  const double tol = 1e-12;
  const int max_iter = 1000;

  for (int i = 0; i < max_iter; i++) {
    double x_new = 0.5 * (x + a / x);
    double diff = x_new - x;
    if (diff < 0) diff = -diff;
    x = x_new;
    if (diff < tol) break;
  }
  return x;
}

void yyerror(const char *s) {
  (void)s;
  fprintf(stderr, "Error de sintaxis\n");
}

int main(int argc, char **argv) {
  if (argc != 2) {
    fprintf(stderr, "Uso: %s <archivo_entrada>\n", argv[0]);
    return 2;
  }

  yyin = fopen(argv[1], "r");
  if (!yyin) {
    fprintf(stderr, "No se pudo abrir '%s': %s\n", argv[1], strerror(errno));
    return 2;
  }

  int rc = yyparse();
  fclose(yyin);
  return rc == 0 ? 0 : 1;
}

