#include <stdio.h>

const char *global_flag = "LAB_SECRET_KEY_9921";

void helper_function(void) {
    puts("[+] Inside helper_function()");
}

int main(void) {
    printf("Static analysis lab sample\n");
    helper_function();
    return 0;
}
