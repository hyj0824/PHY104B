from pathlib import Path
from functools import wraps

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm

# 要有 图名称、轴名称、轴单位和轴刻度 ！！！
# 默认的区间(bin)是左开右闭


def print_gen_banner(func):
    """在 gen 函数调用前后打印分隔符和函数说明。"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        description = (func.__doc__ or "无函数说明").strip()
        print("\n" + "=" * 60)
        print(f"开始执行: {func.__name__}")
        print(f"函数说明: {description}")
        print()
        result = func(*args, **kwargs)
        print()
        return result

    return wrapper


@print_gen_banner
def gen_frequency_histogram(samples: np.ndarray, dir: Path) -> None:
    """
    根据原始数据各区间频数，画出统计直方图
    """

    # 计算组距和组数，确定直方图的x轴范围和刻度，对齐到组距的倍数
    bin_width = 0.02
    x_min = float(np.floor(np.min(samples) / bin_width) * bin_width)
    x_max = float(np.ceil(np.max(samples) / bin_width) * bin_width)
    bin_edges = np.arange(x_min, x_max + bin_width, bin_width)

    plt.figure()
    counts, _, patches = plt.hist(
        samples,
        bins=bin_edges,
        density=False,
        alpha=0.8,
        color="#4C78A8",
        edgecolor="white",
    )

    print("[频数]")
    for i in counts:
        print(f"[{i:.0f}]")

    labels = [f"{v:.0f}" if v > 0 else "" for v in counts]
    plt.bar_label(patches, labels=labels, padding=2, fontsize=8, color="#333333")

    plt.title("节拍器时间频数统计直方图")
    plt.xlabel("测量值 / s")
    plt.ylabel("频数 / 次")
    plt.xlim(x_min, x_max)
    plt.grid(alpha=0.2, linestyle="--")
    plt.tight_layout()
    plt.savefig(dir / "节拍器时间频数统计直方图.svg", format="svg")
    plt.show()


@print_gen_banner
def gen_normal_distribution_and_histogram(samples: np.ndarray, dir: Path) -> None:
    """
    根据各区间概率密度统计结果画出统计直方图，并叠加正态分布曲线
    """

    # 计算组距和组数，确定直方图的x轴范围和刻度，对齐到组距的倍数
    bin_width = 0.02
    x_min = float(np.floor(np.min(samples) / bin_width) * bin_width)
    x_max = float(np.ceil(np.max(samples) / bin_width) * bin_width)
    bin_edges = np.arange(x_min, x_max + bin_width, bin_width)

    plt.figure()
    density_values, bins, patches = plt.hist(
        samples,
        bins=bin_edges,
        density=True,
        alpha=0.8,
        color="#4C78A8",
        edgecolor="white",
        label="测量数据分布",
    )

    print("[区间], [概率], [概率密度],")
    for i in range(len(density_values)):
        print(
            f"[$({bin_edges[i]:.2f}, {bin_edges[i + 1]:.2f}]$], [{density_values[i] * bin_width:.4f}], [{density_values[i]:.4f}],"
        )

    labels = [f"{v:.3f}" if v > 0 else "" for v in density_values]
    plt.bar_label(patches, labels=labels, padding=2, fontsize=8, color="#333333")

    plt.title("节拍器时间概率密度直方图")
    plt.xlabel("测量值 / s")
    plt.ylabel("概率密度 / 1/s")
    plt.xlim(x_min, x_max)
    plt.grid(alpha=0.2, linestyle="--")
    plt.tight_layout()
    plt.savefig(dir / "节拍器时间概率密度直方图.svg", format="svg")

    # 画出区间中值对应的正态分布函数值连线
    mu = float(np.mean(samples))
    sigma = float(np.std(samples, ddof=1))
    bin_centers = (bins[:-1] + bins[1:]) / 2  # 计算区间中值采样点
    y = norm.pdf(bin_centers, loc=mu, scale=sigma)
    plt.plot(
        bin_centers,
        y,
        "o-",
        color="#E45756",
        linewidth=1.8,
        markersize=4,
        label="区间中值对应的正态分布",
    )

    print("[$T$], [$f(T)$],")
    for i in range(len(bin_centers)):
        print(f"[${bin_centers[i]:.3f}$], [${y[i]:.4f}$],")

    plt.title("实验分布与正态分布对比图")
    plt.xlabel("测量值 / s")
    plt.ylabel("概率密度 / 1/s")
    plt.xlim(x_min, x_max)
    plt.grid(alpha=0.2, linestyle="--")
    plt.legend()
    plt.tight_layout()
    plt.savefig(dir / "实验分布与正态分布对比图.svg", format="svg")


@print_gen_banner
def cal_statistics(samples: np.ndarray) -> None:
    # 数据个数 平均值 标准差 最大值 中间值 最小值 极差
    count = len(samples)
    mean = np.mean(samples)
    std_dev = np.std(samples, ddof=1)
    max_val = np.max(samples)
    median = np.median(samples)
    min_val = np.min(samples)
    range_val = max_val - min_val
    print("[数据个数], [平均值], [标准差], [最大值], [中间值], [最小值], [极差],")
    print(
        f"[{count}], [{mean:.4f}], [{std_dev:.4f}], [{max_val:.4f}], [{median:.4f}], [{min_val:.4f}], [{range_val:.4f}],"
    )


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data.csv"

    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    df = pd.read_csv(csv_path)

    # Drop the row index column and flatten all 200 samples into one vector.
    samples = df.drop(columns=["Row"]).to_numpy(dtype=float).reshape(-1)

    gen_frequency_histogram(samples, base_dir)
    gen_normal_distribution_and_histogram(samples, base_dir)
    cal_statistics(samples)


if __name__ == "__main__":
    main()
