import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

class CollegeVisualizer:
    """A class to handle visualization of college datasets."""
    
    def __init__(self, file_path: str):
        """
        Initialize the CollegeVisualizer with a dataset.
        
        Args:
            file_path (str): Path to the CSV dataset file
        """
        self.df = pd.read_csv(file_path)
        self._preprocess_data()
        self._set_theme()
    
    def _preprocess_data(self) -> None:
        """Preprocess the data by cleaning application volume column."""
        self.df["application_volume"] = (
            self.df["application_volume"].astype(str)
            .str.replace(",", "")
            .astype(int)
        )
    
    def _set_theme(self) -> None:
        """Set the seaborn theme and palette."""
        sns.set_theme(style="whitegrid", palette="muted")
    
    def plot_correlation_heatmap(self) -> None:
        """Create a correlation heatmap of numeric columns."""
        plt.figure(figsize=(8, 5))
        sns.heatmap(
            self.df.select_dtypes(include='number').corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )
        plt.title("Correlation Heatmap of College Metrics")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/correlation_heatmap.png", dpi=300)    

    def plot_selectivity_score_vs_4yr_graduation(self) -> None:
        """Create a scatter plot of selectivity score vs 4-year graduation rate."""
        if "selectivity_score" not in self.df.columns:
            self.df["selectivity_score"] = 1 / self.df["admission_rate"]
        
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="selectivity_score",
            y="graduate_rate_4yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Selective Score vs 4-Year Graduation Rate")
        plt.xlabel("Selectivity Score")
        plt.ylabel("4-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/selectivity_score_vs_4yr_graduation.png", dpi=300)
    
    def plot_selectivity_score_vs_6yr_graduation(self) -> None:
        """Create a scatter plot of selectivity score vs 6-year graduation rate."""
        if "selectivity_score" not in self.df.columns:
            self.df["selectivity_score"] = 1 / self.df["admission_rate"]
        
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="selectivity_score",
            y="graduate_rate_6yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Selective Score vs 6-Year Graduation Rate")
        plt.xlabel("Selectivity Score")
        plt.ylabel("6-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/selectivity_score_vs_6yr_graduation.png", dpi=300)
    
    def plot_admission_vs_6yr_graduation(self) -> None:
        """Create a scatter plot of admission rate vs 6-year graduation rate."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="admission_rate",
            y="graduate_rate_6yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Admission Rate vs 6-Year Graduation Rate")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/admission_vs_6yr_graduation.png", dpi=300)
        
        plt.ylabel("4-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/selectivity_score_vs_4yr_graduation.png", dpi=300)
    
    def plot_admission_rate_vs_4yr_graduation(self) -> None:
        """Create a scatter plot of admission rate vs 4-year graduation rate."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="admission_rate",
            y="graduate_rate_4yr",
            hue="colleges",
            data=self.df,
            s=100
        )
        plt.title("Admission Rate vs 4-Year Graduation Rate")
        plt.xlabel("Admission Rate (%)")
        plt.ylabel("4-Year Graduation Rate (%)")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/admission_rate_vs_4yr_graduation.png", dpi=300)

    def plot_tuition_vs_4yr_graduation_dual(self) -> None:
        """Create a dual-axis plot of tuition cost vs 4-year graduation rate by college."""
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        ax1.set_xlabel("College")
        ax1.set_ylabel("Tuition Cost ($)", color="tab:blue")
        ax1.bar(self.df["colleges"], self.df["tuition_cost"], color="tab:blue", alpha=0.7, label="Tuition Cost")
        ax1.tick_params(axis="y", labelcolor="tab:blue")
        ax1.set_xticklabels(self.df["colleges"], rotation=45, ha="right")
        
        ax2 = ax1.twinx()
        ax2.set_ylabel("4-Year Graduation Rate (%)", color="tab:orange")
        ax2.plot(self.df["colleges"], self.df["graduate_rate_4yr"], color="tab:orange", marker="o", linewidth=2, label="4-Year Graduation Rate")
        ax2.tick_params(axis="y", labelcolor="tab:orange")
        
        plt.title("Tuition Cost vs 4-Year Graduation Rate by College")
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/tuition_vs_4yr_graduation_dual.png", dpi=300) 
    
    def plot_tuition_vs_6yr_graduation_dual(self) -> None:
        """Create a dual-axis plot of tuition cost vs 6-year graduation rate by college."""
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        ax1.set_xlabel("College")
        ax1.set_ylabel("Tuition Cost ($)", color="tab:blue")
        ax1.bar(self.df["colleges"], self.df["tuition_cost"], color="tab:blue", alpha=0.7, label="Tuition Cost")
        ax1.tick_params(axis="y", labelcolor="tab:blue")
        ax1.set_xticklabels(self.df["colleges"], rotation=45, ha="right")
        
        ax2 = ax1.twinx()
        ax2.set_ylabel("6-Year Graduation Rate (%)", color="tab:orange")
        ax2.plot(self.df["colleges"], self.df["graduate_rate_6yr"], color="tab:orange", marker="o", linewidth=2, label="6-Year Graduation Rate")
        ax2.tick_params(axis="y", labelcolor="tab:orange")
        
        plt.title("Tuition Cost vs 6-Year Graduation Rate by College")
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/tuition_vs_6yr_graduation_dual.png", dpi=300)
    
    def plot_cohort_size_vs_4yr_graduation_dual(self) -> None:
        """Create a dual-axis plot of cohort size vs 4-year graduation rate by college."""
        if "cohort_size" not in self.df.columns:
            self.df["cohort_size"] = self.df["application_volume"] * self.df["admission_rate"]
        
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        ax1.set_xlabel("College")
        ax1.set_ylabel("Cohort Size", color="tab:blue")
        ax1.bar(self.df["colleges"], self.df["cohort_size"], color="tab:blue", alpha=0.7, label="Cohort Size")
        ax1.tick_params(axis="y", labelcolor="tab:blue")
        ax1.set_xticklabels(self.df["colleges"], rotation=45, ha="right")
        
        ax2 = ax1.twinx()
        ax2.set_ylabel("4-Year Graduation Rate (%)", color="tab:orange")
        ax2.plot(self.df["colleges"], self.df["graduate_rate_4yr"], color="tab:orange", marker="o", linewidth=2, label="4-Year Graduation Rate")
        ax2.tick_params(axis="y", labelcolor="tab:orange")
        
        plt.title("Cohort Size vs 4-Year Graduation Rate by College")
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/cohort_size_vs_4yr_graduation_dual.png", dpi=300)
    
    def plot_cohort_size_vs_6yr_graduation_dual(self) -> None:
        """Create a dual-axis plot of cohort size vs 6-year graduation rate by college."""
        if "cohort_size" not in self.df.columns:
            self.df["cohort_size"] = self.df["application_volume"] * self.df["admission_rate"]
        
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        ax1.set_xlabel("College")
        ax1.set_ylabel("Cohort Size", color="tab:blue")
        ax1.bar(self.df["colleges"], self.df["cohort_size"], color="tab:blue", alpha=0.7, label="Cohort Size")
        ax1.tick_params(axis="y", labelcolor="tab:blue")
        ax1.set_xticklabels(self.df["colleges"], rotation=45, ha="right")
        
        ax2 = ax1.twinx()
        ax2.set_ylabel("6-Year Graduation Rate (%)", color="tab:orange")
        ax2.plot(self.df["colleges"], self.df["graduate_rate_6yr"], color="tab:orange", marker="o", linewidth=2, label="6-Year Graduation Rate")
        ax2.tick_params(axis="y", labelcolor="tab:orange")
        
        plt.title("Cohort Size vs 6-Year Graduation Rate by College")
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/cohort_size_vs_6yr_graduation_dual.png", dpi=300)
    
    def create_all_visualizations(self) -> None:
        """Execute all visualization steps in sequence."""
        self.plot_admission_vs_6yr_graduation()
        self.plot_selectivity_score_vs_4yr_graduation()
        self.plot_selectivity_score_vs_6yr_graduation()
        self.plot_admission_rate_vs_4yr_graduation()
        self.plot_tuition_vs_4yr_graduation_dual()
        self.plot_tuition_vs_6yr_graduation_dual()
        self.plot_cohort_size_vs_4yr_graduation_dual()
        self.plot_cohort_size_vs_6yr_graduation_dual()
        self.plot_correlation_heatmap()
    
    def get_dataframe(self) -> pd.DataFrame:
        """Return the current dataframe."""
        return self.df

if __name__ == "__main__":
    # Example usage
    visualizer = CollegeVisualizer("datasets/college_data.csv")
    visualizer.create_all_visualizations()
