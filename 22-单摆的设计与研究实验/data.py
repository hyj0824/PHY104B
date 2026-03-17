import numpy as np


def cal_statistics(samples: np.ndarray) -> None:
    # 数据个数 平均值 标准差 最大值 中间值 最小值 极差
    count = len(samples)
    mean = np.mean(samples)
    std_dev = np.std(samples, ddof=1)
    max_val = np.max(samples)
    median = np.median(samples)
    min_val = np.min(samples)
    range_val = max_val - min_val
    # print("[数据个数], [平均值], [标准差], [最大值], [中间值], [最小值], [极差],")
    # print(
    #     f"[{count}], [{mean:.4f}], [{std_dev:.4f}], [{max_val:.4f}], [{median:.4f}], [{min_val:.4f}], [{range_val:.4f}],"
    # )

    print("[平均值], [标准差], [中间值], [极差],")
    print(f"[{mean:.4f}], [{std_dev:.4f}], [{median:.4f}], [{range_val:.4f}],")

    # print("== 统计分析 ==")
    # print(f"数据个数：{count}")
    # print(f"平均值：{mean}")
    # print(f"标准差：{std_dev}")
    # print(f"最大值：{max_val}")
    # print(f"中间值：{median}")
    # print(f"最小值：{min_val}")
    # print(f"极差：{range_val}")
    # print()


def main() -> None:

    samples = [
        [[20.00], [20.02], [20.00], [20.00], [19.98]],  # D
        [[64.75], [64.80], [64.78], [64.73], [64.75]],  # L
        [[64.96], [65.03], [65.07], [65.00], [65.06]],  # t
    ]

    print(samples)

    cal_statistics(samples[0])
    cal_statistics(samples[1])
    cal_statistics(samples[2])


if __name__ == "__main__":
    main()
