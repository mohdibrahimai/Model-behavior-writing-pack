"""
Generate a simple dashboard chart showing alignment as bars and latency as a line.
Reads data from data.csv and falls back to default values if missing.
Saves the plot as dashboard.png in the same directory.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """Load alignment and latency data for baseline and quoted_spans.

    Returns a dict mapping variant names to dicts with alignment and latency_ms.
    Uses fallback values if files are missing or incomplete.
    """
    # Default fallback values
    data = {
        "baseline": {"alignment": 0.61, "latency_ms": 820},
        "quoted_spans": {"alignment": 0.72, "latency_ms": 874},
    }
    base_dir = os.path.dirname(__file__)
    data_csv = os.path.join(base_dir, "data.csv")
    if os.path.exists(data_csv):
        try:
            df = pd.read_csv(data_csv)
            for _, row in df.iterrows():
                variant = str(row.get("variant")).strip()
                if variant in data:
                    # update values if both fields present
                    try:
                        alignment = float(row.get("alignment"))
                        latency = float(row.get("latency_ms"))
                        data[variant]["alignment"] = alignment
                        data[variant]["latency_ms"] = latency
                    except (TypeError, ValueError):
                        # ignore invalid entries
                        pass
        except Exception:
            # fall back silently
            pass
    return data


def make_chart(values):
    """Create and save the alignment vs latency chart.

    Args:
        values: dict mapping variant names to metrics.
    """
    variants = ["baseline", "quoted_spans"]
    alignment = [values[v]["alignment"] for v in variants]
    latency = [values[v]["latency_ms"] for v in variants]
    # Compute deltas (quoted_spans relative to baseline)
    delta_alignment_pp = (alignment[1] - alignment[0]) * 100
    delta_latency_pct = ((latency[1] - latency[0]) / latency[0]) * 100
    # Create plot
    fig, ax1 = plt.subplots(figsize=(12.8, 7.2))
    x = range(len(variants))
    # Bars for alignment
    ax1.bar(x, alignment)
    ax1.set_ylabel("Alignment (0–1)")
    ax1.set_xlabel("Variant")
    ax1.set_xticks(x)
    ax1.set_xticklabels(variants)
    ax1.set_ylim(0, 1)
    # Line for latency
    ax2 = ax1.twinx()
    ax2.plot(x, latency, marker="o")
    ax2.set_ylabel("Latency (ms)")
    ax2.set_ylim(0, max(latency) * 1.1)
    # Annotate deltas near quoted_spans bar and point
    ax1.annotate(f"+{delta_alignment_pp:.1f} pp", xy=(1, alignment[1]), xytext=(0, 8), textcoords="offset points", ha="center")
    ax2.annotate(f"+{delta_latency_pct:.1f}%", xy=(1, latency[1]), xytext=(0, -15), textcoords="offset points", ha="center")
    # Title
    ax1.set_title("Alignment (bars) + Latency (line)")
    fig.tight_layout()
    # Save
    out_path = os.path.join(os.path.dirname(__file__), "dashboard.png")
    fig.savefig(out_path)
    plt.close(fig)


def main():
    values = load_data()
    make_chart(values)


if __name__ == "__main__":
    main()