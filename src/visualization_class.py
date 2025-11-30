import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
    
    def plot_admission_rates(self) -> None:
        """Create a bar plot of admission rates by college."""
        plt.figure(figsize=(10, 6))
        sns.barplot(x="admission_rate", y="colleges", data=self.df, color="skyblue")
        plt.title("Admission Rates by College")
        plt.tight_layout()
        plt.savefig("figures/admission_rates_by_college.png", dpi=300)
        plt.show()
    
    def plot_admission_vs_graduation(self) -> None:
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
        plt.savefig("figures/admission_vs_graduation.png", dpi=300)
        plt.show()
    
    def plot_pairplot(self) -> None:
        """Create a pairplot of numeric columns."""
        plt.figure(figsize=(10, 10))
        sns.pairplot(self.df.select_dtypes(include='number'), diag_kind="kde")
        plt.suptitle("Pairplot of College Metrics", y=1.001)
        plt.tight_layout()
        plt.savefig("figures/pairplot_college_metrics.png", dpi=300)
        plt.show()
    
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
        plt.savefig("figures/correlation_heatmap.png", dpi=300)
        plt.show()
    
    def plot_application_vs_admission(self) -> None:
        """Create a scatter plot of application volume vs admission rate."""
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            x="application_volume",
            y="admission_rate",
            hue="colleges",
            data=self.df,
            s=120
        )
        plt.title("Application Volume vs Admission Rate")
        plt.tight_layout()
        plt.savefig("figures/application_vs_admission.png", dpi=300)
        plt.show()
    
    def plot_graduation_rates_comparison(self) -> None:
        """Create a bar plot comparing 4-year vs 6-year graduation rates."""
        plt.figure(figsize=(10, 6))
        df_melt = self.df.melt(
            id_vars="colleges",
            value_vars=["graduate_rate_4yr", "graduate_rate_6yr"],
            var_name="Graduation Type",
            value_name="Rate"
        )
        sns.barplot(x="Rate", y="colleges", hue="Graduation Type", data=df_melt)
        plt.title("4-Year vs 6-Year Graduation Rates by College")
        plt.tight_layout()
        plt.savefig("figures/graduation_rates_comparison.png", dpi=300)
        plt.show()
    
    def create_all_visualizations(self) -> None:
        """Execute all visualization steps in sequence."""
        self.plot_admission_rates()
        self.plot_admission_vs_graduation()
        self.plot_pairplot()
        self.plot_correlation_heatmap()
        self.plot_application_vs_admission()
        self.plot_graduation_rates_comparison()
    
    def save_cleaned_data(self, output_path: str = "datasets/college_data_cleaned.csv") -> None:
        """
        Save the cleaned dataset to a CSV file.
        
        Args:
            output_path (str): Path where the cleaned dataset should be saved
        """
        self.df.to_csv(output_path, index=False)
    
    def get_dataframe(self) -> pd.DataFrame:
        """Return the current dataframe."""
        return self.df


if __name__ == "__main__":
    # Example usage
    visualizer = CollegeVisualizer("datasets/college_data.csv")
    visualizer.create_all_visualizations()
    visualizer.save_cleaned_data()
