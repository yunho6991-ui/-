"""카드 던전 난이도 모의실험 (docs/dungeon-game.md "난이도 곡선").
가상의 유저가 매일 소환하고 탐험할 때, n일 뒤 최고 층이 어떻게 되는지 본다.
실행: python3 tools/dungeon_sim.py            (기본: 몬스터 = 130 × 1.08^층)
     python3 tools/dungeon_sim.py 150 1.085   (다른 값 시험)
"""
import random, statistics as st
GR=['N','R','SR','SSR','UR','LR']; P=[60,28,9,2.5,0.45,0.05]; BASE=[10,25,60,150,400,1000]
PER_ZONE=[3,3,3,2,1,1]   # cards per grade per zone
ZONES=5; ELEM=5
def card_ids(zones):
    ids=[]
    for z in range(zones):
        for g,n in enumerate(PER_ZONE):
            for k in range(n): ids.append((z,g,k))
    return ids
def win_p(r):
    if r>=1.5: return .98
    if r>=1.0: return .85
    if r>=0.7: return .50
    if r>=0.5: return .20
    return .05
def sim(base,g,days,summ_per_day=6,runs_per_day=3,seed=0,first_day_summons=10):
    rnd=random.Random(seed)
    coll={}  # id->(stars, elem)
    best=0; ckpt=0; pity=0
    elem_of={}
    hist=[]
    for d in range(days):
        zones=min(ZONES, best//10+1)
        pool={}
        for cid in card_ids(zones):
            pool.setdefault(cid[1],[]).append(cid)
            elem_of.setdefault(cid, rnd.randrange(ELEM))
        n= summ_per_day + (first_day_summons if d==0 else 0)
        for _ in range(n):
            pity+=1
            if pity>=100: gi=4; pity=0
            else:
                gi=rnd.choices(range(6),P)[0]
                if gi>=4: pity=0
            newest=zones-1
            cands=pool[gi]
            w=[2 if c[0]==newest and zones>1 else 1 for c in cands]
            c=rnd.choices(cands,w)[0]
            coll[c]=min(5,coll.get(c,0)+1)
        # boss cards count to dex
        uniq=len(coll)+ (ckpt//10)
        zone_done=sum(1 for z in range(zones) if all((z,g_,k) in coll for g_,n in enumerate(PER_ZONE) for k in range(n)))
        dex=1+0.005*uniq+0.05*zone_done
        for _ in range(runs_per_day):
            f=ckpt+1
            while True:
                fe=rnd.randrange(ELEM)
                powers=[]
                for c,s in coll.items():
                    pw=BASE[c[1]]*(1+0.3*(s-1))
                    if elem_of[c]==(fe+1)%ELEM: pw*=1.5
                    powers.append(pw)
                party=sum(sorted(powers,reverse=True)[:5])*dex
                mon=base*g**f
                if rnd.random()<win_p(party/mon):
                    if f%10==0: ckpt=max(ckpt,f)
                    best=max(best,f); f+=1
                    if f>500: break
                else: break
        hist.append(best)
    return hist
def summary(base,g,n=400):
    days=[1,3,7,14,30,60]
    res={d:[] for d in days}
    for s in range(n):
        h=sim(base,g,60,seed=s)
        for d in days: res[d].append(h[d-1])
    out=[]
    for d in days:
        v=sorted(res[d]); out.append((d,v[len(v)//2],v[int(len(v)*.9)],v[-1]))
    return out
import sys
if __name__=="__main__":
    base=float(sys.argv[1]) if len(sys.argv)>1 else 130
    g=float(sys.argv[2]) if len(sys.argv)>2 else 1.08
    print(f"몬스터 전투력 = {base:g} × {g:g}^층  (유저 200명, 하루 소환 6회·첫날 +10, 탐험 3회)")
    print("일차 | 중간값 | 상위10% | 가장 운 좋은 사람")
    for d,med,p90,mx in summary(base,g,200):
        print(f"{d:>4} | {med:>5}층 | {p90:>6}층 | {mx:>4}층")
