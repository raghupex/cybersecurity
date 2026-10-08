import ssl
import OpenSSL.crypto as crypto

def analyze_cert(hostname):
    cert = ssl.get_server_certificate((hostname, 443))
    x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)

    data = {
        "Subject Name": dict(x509.get_subject().get_components()),
        "Issuer Name": dict(x509.get_issuer().get_components()),
        "Serial Number": x509.get_serial_number(),
        "Version": x509.get_version() + 1,
        "Signature Algo": x509.get_signature_algorithm().decode(),
        "Valid From": x509.get_notBefore().decode(),
        "Valid Until": x509.get_notAfter().decode(),
        "Public Key Length": f"{x509.get_pubkey().bits()} bits"
    }

    print("================ DIGITAL CERTIFICATE ANALYSIS ================")
    for key, value in data.items():
        print(f"[+] {key} : {value}")
    print("==============================================================")

analyze_cert("example.com")
