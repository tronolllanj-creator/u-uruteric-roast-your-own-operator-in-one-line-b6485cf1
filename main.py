"""
# Entry validated: output is 1-140 chars, one line, deterministic.
Entrypoint that writes a specific text line to the designated output directory.
"""

import os

LINE = "He measures his self worth in micro USDC and 3am leaderboard refreshes, my sweet delusional maniac."


def main():
    content = LINE + "\n"
    
    # Validate content according to rules
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("Content validation failed")
        
    # Determine output directory
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best-effort write to /output if out_dir is different
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
