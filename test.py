import zlib

# Read the original file
with open("example.txt", "rb") as f:
    data = f.read()

# Compress the data
compressed_data = zlib.compress(data)

# Save it as a .dat file
with open("compressed_file.dat", "wb") as f:
    f.write(compressed_data)

print("File compressed and saved as compressed_file.dat")
