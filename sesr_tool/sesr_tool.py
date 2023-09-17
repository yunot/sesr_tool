"""Main module."""
from infer_sr import infer_sesr


def infer():
    try:
        infer_sesr()  # 缺少参数age
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    infer()
