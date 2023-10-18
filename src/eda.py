from data_collection import Rawdata
import seaborn as sns
import matplotlib.pyplot as plt


class EDA:
    def __init__(self, extractedtext):
        self.extractedtext = extractedtext

    def aboutdata(self):
        return self.extractedtext.info()

    def summarystatistic(self):
        return self.extractedtext.describe()

    def shapeofdataframe(self):
        return self.extractedtext.shape

    def correlation_heatmap(self):
        correlation_matrix = self.extractedtext.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()

    def histogram_with_kde(self):
        sns.distplot(self.extractedtext['target'], hist=True, kde=True,
                     bins=int(30), color='darkblue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 2})
        plt.title(f'Distribution of target')
        plt.xlabel('target')
        plt.ylabel('Density')
        plt.show()


if __name__ == "__main__":
    Data = EDA(Rawdata)

    # Information about the dataframe
    print(Data.aboutdata())

    # Summary statistics
    print(Data.summarystatistic())

    # Shape of the dataframe
    print(Data.shapeofdataframe())

    # Correlation Heatmap
    Data.correlation_heatmap()

    # Histogram of output
    # eda.histogram_with_kde()
