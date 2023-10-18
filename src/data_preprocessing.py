from data_collection import Rawdata

class Preprocessing:
    def __int__(self , data):
        self.data = data

    def checkmissingnumber(self):
        return self.data.isnull().sum()

    def dealingwithmissingvalues(self):
        """
            methods that remove columns with many missing values.
        """
        data = self.data
        selectedcol = 'cement'
        threshold = len(data[selectedcol])  # Set the threshold for missing values
        if  data.isnull().sum().sum() != 0:
            # Check which columns have more than 20 missing values
            columns_to_drop = data.columns[data.isnull().sum() >= threshold]
            # Drop the identified columns
            data = data.drop(columns=columns_to_drop)
            return  data
        else:
            return data

    def dealingwithincorrectcol(self):
        datawithnomissingvalues = self.dealingwithmissingvalues()








if __name__ == "__main__":
    p1 = Preprocessing(Rawdata)