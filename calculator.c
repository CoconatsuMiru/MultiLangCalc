#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int a, b;
    char op;
    sscanf(argv[1], "%d %c %d", &a, &op, &b);
    switch(op) {
        case '+': printf("%d\n", a + b); break;
        case '-': printf("%d\n", a - b); break;
        case '*': printf("%d\n", a * b); break;
        case '/': if (b != 0) printf("%d\n", a / b); else printf("DIV_ZERO_ERROR\n"); break;
        default: printf("INVALID_OP\n");
    }
    return 0;
}
