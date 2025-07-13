import pandas as pd


def inspect_file(path: str, encoding: str = "cp949"):
    try:
        print(f"\n📄 파일: {path}")
        df: pd.DataFrame = pd.read_csv(
            path, encoding=encoding, delimiter=None, engine="python", header=None
        )
        print("➡ 열 수:", df.shape[1])
        print("➡ 미리보기:")
        print(df.head())
    except Exception as e:
        print(f"❌ 읽기 실패: {e}")


# 파일 경로
paths = ["data/해남기온.csv", "data/해남강수량.csv", "data/해남습도.csv"]

for file_path in paths:
    inspect_file(file_path)
