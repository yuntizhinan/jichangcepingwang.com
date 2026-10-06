import glob
import os

target_dir = r"C:\Users\PC\.gemini\antigravity-ide\scratch\airport-review-blog"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace("闪连评测", "闪电机场评测")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Updated {len(html_files)} files successfully.")
