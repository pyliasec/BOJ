import os
import shutil
import re

def main():
    base = os.getcwd()
    print(f"기본 디렉토리: {base}")

    LANGS = {
        'c': 'C',
        'cpp': 'Cpp',
        'py': 'Python3',
        'go': 'Go'
    }

    COMMENT_PATTERNS = {
        'c': re.compile(r'^\s*//'),
        'cpp': re.compile(r'^\s*//'),
        'py': re.compile(r'^\s*#'),
        'go': re.compile(r'^\s*//')
    }

    for root, _, files in os.walk(base):
        for fname in files:
            parts = fname.rsplit('.', 1)
            if len(parts) != 2:
                continue
            num_part, ext = parts
            ext = ext.lower()
            if not num_part.isdigit() or ext not in LANGS:
                continue

            src = os.path.join(root, fname)
            num = int(num_part)
            start = (num // 10000) * 10000
            end = start + 9999
            range_folder = f"{start}~{end}"
            lang_folder = LANGS[ext]

            try:
                with open(src, encoding='utf-8') as f:
                    first_line = f.readline().lstrip('\ufeff').rstrip('\n')
            except Exception as e:
                print(f"[경고] 파일 읽기 실패: {src}, {e}")
                first_line = ''

            pattern = COMMENT_PATTERNS[ext]
            status = 'unsolved' if pattern.match(first_line or '') else 'solved'

            dst_dir = os.path.join(base, lang_folder, range_folder, status)
            os.makedirs(dst_dir, exist_ok=True)
            dst = os.path.join(dst_dir, fname)

            if os.path.abspath(src) == os.path.abspath(dst):
                continue

            print(f"이동: {src} -> {dst}")
            shutil.move(src, dst)

if __name__ == '__main__':
    main()