import pandas as pd

class drift_detector():

    def __init__(self, old_data, new_data):
        self.old_data = old_data
        self.new_data = new_data

    def validate_logic(self):
        # check count of columns
        
        v1 = (len(self.old_data.columns) == len(self.new_data.columns))

        # check same columns are present 
        v2 = (list(self.old_data.columns) == list(self.new_data.columns))

        if (v1 == False) or (v2 == False):
            raise ColumnMismatchError('Specific Reason')
        
        return (v1 and v2)
    
class ColumnMismatchError(Exception):
    pass


if __name__ == "__main__":
    old_data = pd.read_csv('reference_dataset.csv')
    # print('\nOld Data\n',old_data.head())

    new_data = pd.read_csv('current_dataset.csv')
    # print('\nNew Data\n',new_data.head())
    
    
    cls = drift_detector(old_data, new_data)

    try:
        if True == cls.validate_logic():
            print('We can continue.')
    except ColumnMismatchError as e:
        print("Validation failed:", e)
