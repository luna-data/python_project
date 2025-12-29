import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

plt.rcParams["font.family"] = "Malgun Gothic"  # 윈도우
plt.rcParams["axes.unicode_minus"] = False


# =========================
# 0) 설정: 폴더만 바꾸면 끝
# =========================
DATA_DIR = Path(r"C:\학교\public_medical_institution")  # ✅ 본인 폴더 경로

FILES = {
    "base": "공공의료기관 현황_일반현황.csv",
    "beds": "공공의료기관 현황_시설(병상)현황.csv",
    "staff": "공공의료기관 현황_인력현황.csv",
    "equip": "공공의료기관 현황_장비현황.csv",
    "spec": "공공의료기관 현황_전문의현황.csv",
}

# -------------------------
# 1) 안전 로더 (인코딩/구분자/공백 대응)
# -------------------------
def read_kcsv(path: Path) -> pd.DataFrame:
    # 인코딩 후보를 순서대로 시도
    for enc in ("utf-8-sig", "utf-8", "cp949", "euc-kr"):
        try:
            df = pd.read_csv(path, encoding=enc)
            return df
        except Exception:
            pass
    # 마지막 fallback (그래도 안되면 에러를 보여주기)
    return pd.read_csv(path, encoding="cp949")

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.astype(str).str.strip()
    return df

def strip_key_cols(df: pd.DataFrame, key_candidates=("의료기관명", "요양종별")) -> pd.DataFrame:
    df = df.copy()
    for k in key_candidates:
        if k in df.columns:
            df[k] = df[k].astype(str).str.strip()
    return df

def find_first_existing_col(df: pd.DataFrame, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None

def coerce_numeric(series: pd.Series) -> pd.Series:
    # "1,234" 같은 콤마 제거 후 숫자 변환
    s = series.astype(str).str.replace(",", "", regex=False)
    return pd.to_numeric(s, errors="coerce")

# -------------------------
# 2) 데이터 로드
# -------------------------
paths = {k: DATA_DIR / v for k, v in FILES.items()}
for k, p in paths.items():
    if not p.exists():
        raise FileNotFoundError(f"[경로 오류] {k} 파일을 찾을 수 없어요: {p}")

base = strip_key_cols(clean_columns(read_kcsv(paths["base"])))
beds = strip_key_cols(clean_columns(read_kcsv(paths["beds"])))
staff = strip_key_cols(clean_columns(read_kcsv(paths["staff"])))
equip = strip_key_cols(clean_columns(read_kcsv(paths["equip"])))
spec = strip_key_cols(clean_columns(read_kcsv(paths["spec"])))

# -------------------------
# 3) 시도 컬럼 만들기 (주소 컬럼 자동 탐색)
# -------------------------
addr_col = find_first_existing_col(base, ["주소", "소재지", "소재지주소", "기관주소", "도로명주소", "지번주소"])
if addr_col is None:
    # 주소가 없다면 시도 분석이 어려워서 안내
    raise KeyError("[컬럼 오류] 일반현황 파일에서 주소/소재지 컬럼을 찾지 못했어요. base.columns를 확인해 주세요.")

base["시도"] = base[addr_col].astype(str).str.split().str[0].str.strip()

# 시도 표기 통일(선택): 서울특별시 -> 서울, 세종특별자치시 -> 세종 등
SIDO_MAP = {
    "서울특별시": "서울", "부산광역시": "부산", "대구광역시": "대구", "인천광역시": "인천",
    "광주광역시": "광주", "대전광역시": "대전", "울산광역시": "울산", "세종특별자치시": "세종",
    "경기도": "경기", "강원도": "강원", "충청북도": "충북", "충청남도": "충남",
    "전라북도": "전북", "전라남도": "전남", "경상북도": "경북", "경상남도": "경남",
    "제주특별자치도": "제주"
}
base["시도"] = base["시도"].replace(SIDO_MAP)

# -------------------------
# 4) 병합: 가능한 경우 (의료기관명+요양종별) 우선, 아니면 의료기관명만
# -------------------------
def safe_merge(left: pd.DataFrame, right: pd.DataFrame, prefer_keys=("의료기관명", "요양종별")) -> pd.DataFrame:
    left = left.copy()
    right = right.copy()

    keys = [k for k in prefer_keys if k in left.columns and k in right.columns]
    if len(keys) == 0:
        raise KeyError("[병합 오류] 병합할 공통 키를 찾지 못했어요. 최소 '의료기관명'이 양쪽에 있어야 합니다.")
    # 키가 2개 있으면 2개로, 아니면 1개로 병합
    return left.merge(right, on=keys, how="left", suffixes=("", "_dup"))

df = base
df = safe_merge(df, beds)
df = safe_merge(df, staff)
df = safe_merge(df, equip)
df = safe_merge(df, spec)

# 중복 컬럼(_dup) 제거(있을 때만)
dup_cols = [c for c in df.columns if c.endswith("_dup")]
if dup_cols:
    df.drop(columns=dup_cols, inplace=True)

# -------------------------
# 5) 시각화 1: 시도별 기관 수
# -------------------------
cnt = df.groupby("시도")["의료기관명"].nunique().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=cnt.index, y=cnt.values)
plt.xticks(rotation=45, ha="right")
plt.title("시도별 공공의료기관 수")
plt.ylabel("기관 수")
plt.xlabel("시도")
plt.tight_layout()
plt.show()

# -------------------------
# 6) 시각화 2: 시도×요양종별 히트맵 (요양종별 컬럼이 있을 때만)
# -------------------------
if "요양종별" in df.columns:
    pivot = df.pivot_table(
        index="시도", columns="요양종별", values="의료기관명",
        aggfunc=pd.Series.nunique, fill_value=0
    )

    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, annot=True, fmt="d")
    plt.title("시도 × 요양종별 공공의료기관 수")
    plt.tight_layout()
    plt.show()
else:
    print("[주의] '요양종별' 컬럼이 없어 히트맵은 건너뜁니다.")

# -------------------------
# 7) 역량지수 만들기: 컬럼명을 자동으로 찾아 최대한 맞춰줌
#    - 허가병상수: '허가병상' 포함 컬럼
#    - CT/MRI: 'CT', 'MRI' 포함 컬럼 (괄호/띄어쓰기 차이 대응)
#    - 전문의: 우선 '전문의'라는 단일 컬럼이 있으면 사용,
#             없으면 전문의현황(과목별) 컬럼들의 합으로 생성
# -------------------------
def find_col_by_keywords(df: pd.DataFrame, keywords):
    # keywords: ["허가", "병상"] 같이 모두 포함되는 컬럼을 우선 찾음
    cols = list(df.columns)
    for c in cols:
        name = str(c)
        ok = True
        for kw in keywords:
            if kw not in name:
                ok = False
                break
        if ok:
            return c
    return None

bed_col = find_col_by_keywords(df, ["허가", "병상"]) or find_col_by_keywords(df, ["병상"])
ct_col  = find_col_by_keywords(df, ["CT"]) or find_col_by_keywords(df, ["단층", "CT"])
mri_col = find_col_by_keywords(df, ["MRI"]) or find_col_by_keywords(df, ["자기", "MRI"])

# 전문의 컬럼 후보
doc_col = None
for candidate in ["전문의", "전문의수", "전문의 수", "전문의현원", "전문의 현원", "전문의(명)"]:
    if candidate in df.columns:
        doc_col = candidate
        break

# 단일 전문의 컬럼이 없으면: "전문의현황" 파일에서 과목별 컬럼을 합산
if doc_col is None:
    # 숫자형으로 보일 만한 '전문의 과목' 컬럼들 추정:
    # 일반적으로 '의료기관명/요양종별' 제외하고 대부분이 과목별 숫자일 가능성이 큼
    exclude = {"의료기관명", "요양종별", "시도", addr_col}
    cand_cols = [c for c in df.columns if c not in exclude]

    # 숫자로 변환했을 때 유효값이 어느 정도 있는 컬럼만 선택
    numeric_like = []
    for c in cand_cols:
        s = coerce_numeric(df[c])
        if s.notna().mean() >= 0.3:  # 30% 이상이 숫자로 변환되면 "숫자 컬럼" 후보
            numeric_like.append(c)

    # 그중에서 "전문의현황" 특성을 가진 컬럼이 많으면 합을 만들어 전문의_total로 사용
    if len(numeric_like) > 0:
        df["전문의_total"] = 0.0
        for c in numeric_like:
            df["전문의_total"] += coerce_numeric(df[c]).fillna(0)
        doc_col = "전문의_total"

# 필요한 컬럼이 하나라도 없으면 역량지수는 만들 수 없으니 안내
need = {"허가병상수": bed_col, "CT": ct_col, "MRI": mri_col, "전문의": doc_col}
missing = [k for k, v in need.items() if v is None]

if missing:
    print("\n[역량지수 생성 건너뜀] 아래 핵심 컬럼을 자동으로 찾지 못했어요:")
    for k in missing:
        print(f" - {k}")
    print("\n👉 해결 방법: df.columns 출력 후, 실제 컬럼명으로 직접 지정해 주세요.")
    print("예) bed_col='허가병상수', ct_col='전산화단층촬영장치(CT)' 처럼요.\n")
    print("현재 df 컬럼 일부 미리보기:")
    print(df.columns.tolist()[:50], "...")

else:
    # 숫자 변환
    df["허가병상수_use"] = coerce_numeric(df[bed_col]).fillna(0)
    df["CT_use"] = coerce_numeric(df[ct_col]).fillna(0)
    df["MRI_use"] = coerce_numeric(df[mri_col]).fillna(0)
    df["전문의_use"] = coerce_numeric(df[doc_col]).fillna(0)

    cols_use = ["허가병상수_use", "전문의_use", "CT_use", "MRI_use"]
    X = df[cols_use].values.astype(float)

    # 표준화(Z-score)
    Z = (X - X.mean(axis=0)) / (X.std(axis=0) + 1e-9)
    df["역량지수"] = Z.mean(axis=1)

    # 시도별 평균 역량지수
    cap = df.groupby("시도")["역량지수"].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=cap.index, y=cap.values)
    plt.xticks(rotation=45, ha="right")
    plt.title("시도별 평균 공공의료 역량지수")
    plt.tight_layout()
    plt.show()

    # 참고: 역량지수 상위 기관 TOP 10
    top10 = df[["시도", "의료기관명", "역량지수"]].dropna().sort_values("역량지수", ascending=False).head(10)
    print("\n[역량지수 TOP 10 기관]")
    print(top10.to_string(index=False))
