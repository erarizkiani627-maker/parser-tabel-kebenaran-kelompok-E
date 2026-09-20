import itertools

def evaluate_expression(expression, var_map):
    # Mengubah operator kapital menjadi sintaks valid Python
    formatted_expr = (
        expression.replace("AND", "and")
        .replace("OR", "or")
        .replace("NOT", "not")
    )
    return eval(formatted_expr, {}, var_map)

def generate_truth_table(expression):
    # Tokenisasi & Deteksi Variabel Otomatis
    tokens = expression.replace("(", " ").replace(")", " ").split()
    operators = {"AND", "OR", "NOT", "and", "or", "not"}
    variables = sorted(list(set([t for t in tokens if t not in operators])))

    n = len(variables)
    combinations = list(itertools.product([True, False], repeat=n))

    print(f"\nEkspresi: {expression}")
    print(f"Jumlah Variabel Detected: {n} ({', '.join(variables)})")
    print(f"Kombinasi Kebenaran: 2^{n} = {len(combinations)} baris\n")

    # Header Tabel
    header = " | ".join(variables) + " | " + expression
    print("=" * len(header))
    print(header)
    print("=" * len(header))

    # Evaluasi dan Tampilan Tabel
    for combo in combinations:
        var_map = dict(zip(variables, combo))
        result = evaluate_expression(expression, var_map)
        
        row_vars = " | ".join(["T" if var_map[v] else "F" for v in variables])
        row_res = "T" if result else "F"
        
        print(f"{row_vars} | {row_res}")
    print("=" * len(header))

# --- UJI COBA SESUAI LAPORAN ---
# Uji Coba 1
generate_truth_table("p AND (q OR NOT r)")

# Uji Coba 2
generate_truth_table("(p OR q) AND NOT (p AND q)")