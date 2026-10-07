"""무협 데이터 검사 (docs/wuxia-data.md).
data/wuxia/**/*.yaml 을 읽어서 ① YAML 형식 ② id 중복 ③ 없는 id를 가리키는 참조를 확인한다.
없는 참조는 "아직 안 만든 것" 목록으로 보여 준다(예시 단계에선 많아도 정상).

실행: python3 tools/wuxia_data_check.py
"""
import glob, os, re, sys
import yaml

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'wuxia')
PREFIX = ('ev_', 'npc_', 'org_', 'ma_', 'pl_', 'fac_', 'tr_', 'lg_', 'end_', 'st_')
ID_RE = re.compile(r'\b(?:%s)[a-z0-9_]+' % '|'.join(PREFIX))


def walk(x, defined, refs, where):
    if isinstance(x, dict):
        if 'id' in x and isinstance(x['id'], str):
            if x['id'] in defined:
                print(f"❌ id 중복: {x['id']} ({where} / {defined[x['id']]})")
            defined[x['id']] = where
        for k, v in x.items():
            if k == 'id':
                continue
            for m in ID_RE.findall(str(k)):
                refs.setdefault(m, where)
            walk(v, defined, refs, where)
    elif isinstance(x, list):
        for v in x:
            walk(v, defined, refs, where)
    elif isinstance(x, str):
        for m in ID_RE.findall(x):
            refs.setdefault(m, where)


def main():
    files = sorted(glob.glob(os.path.join(ROOT, '**', '*.yaml'), recursive=True))
    if not files:
        print("data/wuxia 에 YAML 파일이 없다"); return 1
    defined, refs, bad = {}, {}, 0
    for f in files:
        rel = os.path.relpath(f, ROOT)
        try:
            data = yaml.safe_load(open(f, encoding='utf-8'))
        except yaml.YAMLError as e:
            print(f"❌ YAML 오류: {rel}\n{e}"); bad += 1; continue
        walk(data, defined, refs, rel)
    missing = sorted(r for r in refs if r not in defined)
    print(f"✅ 파일 {len(files)}개 · 정의된 id {len(defined)}개 · 참조 {len(refs)}개")
    if missing:
        by = {}
        for m in missing:
            by.setdefault(m.split('_')[0] + '_', []).append(m)
        print(f"📝 아직 안 만든 것 {len(missing)}개:")
        for p, ids in sorted(by.items()):
            print(f"  {p}: {', '.join(ids)}")
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
