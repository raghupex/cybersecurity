#include <stdio.h>
#include <string.h>
#include <limits.h>

int main(void) {
    char buf[16], input[64];

    printf("==================================================\n");
    printf("=== Memory & Input Vulnerability Demonstration ===\n");
    printf("==================================================\n");

    printf("\n--- 1. Bounded Buffer Overflow Mitigation ---\n");
    printf("Enter input text (max 15 chars): ");
    if (fgets(buf, sizeof(buf), stdin)) {
        buf[strcspn(buf, "\n")] = '\0';
        printf("[+] Bounded Buffer Content: %s\n", buf);
        printf("[+] String Length: %zu bytes (Safe from stack overflow)\n",
               strlen(buf));
    }

    printf("\n--- 2. Integer Overflow & Wrap-Around ---\n");
    printf("[+] Max Unsigned Int (UINT_MAX) : %u\n", UINT_MAX);
    printf("[+] UINT_MAX + 1 (Wrap-around) : %u\n", UINT_MAX + 1U);

    unsigned short s = USHRT_MAX;
    printf("[+] Max Unsigned Short (USHRT_MAX): %u\n", (unsigned)s);
    printf("[+] USHRT_MAX + 1 (Wrap-around) : %u\n",
           (unsigned short)(s + 1));

    printf("\n--- 3. Format String Vulnerability Testing ---\n");
    printf("Enter string with format specifiers (e.g., hello %%x %%p): ");
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = '\0';
        printf("\n[!] UNSAFE PATTERN: printf(input);\n");
        printf(" -> Risk: User specifiers (%%x, %%p) directly execute as format directives.\n");
        printf("[+] SAFE PATTERN : printf(\"%%s\\n\", input);\n");
        printf(" -> Safe Output: %s\n", input);
    }

    printf("\n==================================================\n");
    return 0;
}
