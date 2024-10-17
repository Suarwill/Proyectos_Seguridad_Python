import hashlib
import sys

def hashes(x):
  with open(x, 'rb') as f:
    md5, sha1, sha256 = hashlib.md5(), hashlib.sha1(), hashlib.sha256()
    while chunk := f.read(8192):
      md5.update(chunk)
      sha1.update(chunk)
      sha256.update(chunk)
  return md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()

if __name__ == "__main__":
  if len(sys.argv) != 2: print("Uso: python script.py <ruta_al_archivo>")
  else:
    x = sys.argv[1]
    md5, sha1, sha256 = hashes(x)
    print(f"El hash     MD5 del archivo es: {md5}")
    print(f"El hash   SHA-1 del archivo es: {sha1}")
    print(f"El hash SHA-256 del archivo es: {sha256}")
    input("\npresione para continuar")