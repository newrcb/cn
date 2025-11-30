def calc_parity_bits_length(m):
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r


def insert_parity_bits(data, r):
    # Place r parity bits (0) at positions that are powers of two
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res += '0'
            j += 1
        else:
            res += data[-k]
            k += 1
    return res[::-1]


def set_parity_bits(arr, r):
    n = len(arr)
    arr = list(arr)
    for i in range(r):
        idx = (2 ** i) - 1
        parity = 0
        step = 2 ** (i + 1)
        for j in range(idx, n, step):
            parity += sum(int(arr[k]) for k in range(j, min(j + 2 ** i, n)))
        arr[idx] = str(parity % 2)
    return ''.join(arr)


def encode(data):
    """Return Hamming-encoded string for input data bits (string of '0'/'1')."""
    m = len(data)
    r = calc_parity_bits_length(m)
    arr = insert_parity_bits(data, r)
    return set_parity_bits(arr, r)


def detect_and_correct(codeword):
    """Detect and correct a single-bit error in `codeword`. Returns corrected codeword."""
    n = len(codeword)
    # compute r from codeword length
    r = 0
    while 2 ** r < n + 1:
        r += 1

    arr = list(codeword)
    error_pos = 0
    for i in range(r):
        idx = (2 ** i) - 1
        parity = 0
        step = 2 ** (i + 1)
        for j in range(idx, n, step):
            parity += sum(int(arr[k]) for k in range(j, min(j + 2 ** i, n)))
        if parity % 2 != 0:
            error_pos += 2 ** i

    if error_pos:
        # flip the erroneous bit
        pos = error_pos - 1
        arr[pos] = '1' if arr[pos] == '0' else '0'

    return ''.join(arr)


def extract_data(codeword):
    """Remove parity bits and return original data bits as a string."""
    return ''.join(
        codeword[i] for i in range(len(codeword)) if (i + 1) & i
    )


if __name__ == "__main__":
    data = input("Data bits (e.g. 1011): ").strip()
    encoded = encode(data)
    print("Encoded:", encoded)

    received = input("Received (press Enter to use encoded): ").strip() or encoded
    corrected = detect_and_correct(received)
    print("Corrected:", corrected)