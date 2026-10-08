CYBER SECURITY LAB — PROGRAM FILES ONLY

Python requirements:
    pip install pycryptodome pyOpenSSL

Run Python:
    python Exp1_RSA_AES_SHA256.py
    python Exp2_Digital_Certificate.py
    python Exp3_2FA_TOTP.py
    python Exp4_Privilege_Escalation.py
    python Exp6_DVWA_Vulnerability_Analysis.py

Compile/run C:
    gcc -o exp5 Exp5_Memory_Input_Vulnerabilities.c
    ./exp5

    gcc -O0 -o sample9 Exp9_Static_Analysis.c
    file sample9
    strings sample9 | grep -E 'Static|LAB_SECRET|helper|printf'
    objdump -t sample9 | grep -E 'main|helper_function|global_flag'
    objdump -d sample9 | grep -A 20 "<main>:"

Linux:
    chmod +x Exp7_Wazuh_Agent.sh Exp8_Snort_Monitoring.sh
    ./Exp7_Wazuh_Agent.sh
    ./Exp8_Snort_Monitoring.sh

Notes:
- Exp1 AES/RSA ciphertext changes because random keys are generated.
- Exp2 certificate values can change when the live certificate changes.
- Exp3 TOTP changes every 30 seconds.
- Exp7 requires a reachable Wazuh manager at the configured IP.
- Exp8 requires Snort 3, a valid configuration, local.rules, and the eth0 interface.
