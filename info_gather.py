import socket
import ssl
import requests


def gather_info(domain: str) -> None:
    print(f"=== Info Publik: {domain} ===\n")

    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address   : {ip}")
    except socket.gaierror:
        print("Gagal resolve domain — periksa penulisan domainnya.")
        return

    try:
        r = requests.get(f"https://swap.gg", timeout=5)
        print(f"Status Code  : {r.status_code}")
        print(f"Server       : {r.headers.get('Server', 'tidak diketahui')}")
        print(f"X-Powered-By : {r.headers.get('X-Powered-By', 'tidak diketahui')}")
    except requests.exceptions.RequestException as e:
        print(f"Gagal HTTP request: {e}")

    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                issuer = dict(x[0] for x in cert.get("issuer", []))
                print(f"SSL Issuer   : {issuer.get('organizationName', issuer)}")
                print(f"SSL Expiry   : {cert.get('notAfter')}")
    except Exception as e:
        print(f"Gagal ambil info SSL: {e}")


if __name__ == "__main__":
    gather_info("swap.gg") 