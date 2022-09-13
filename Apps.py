from csv import reader

class Apps:
    def __init__(self, dataset):
        self.name_dataset = dataset
        self.opened_file = open(dataset, encoding="utf8")
        self.read_file = reader(self.opened_file)
        self.file = list(self.read_file)
        self.header = self.file[0]
        self.data = self.file[1:]
        


    def explore_data(self, start, end, rows_and_columns=False):
         dataset_slice = self.data[start:end]    
         for row in dataset_slice:
            print(row)
            print('\n') 
        
         if rows_and_columns:
            print('Number of rows:', len(self.data))
            print('Number of columns:', len(self.data[0]))

    def delete_row(self, number_row):
        del self.data[number_row]

    def remove_duplicate(self):
        reviews_max = {}
        for app in self.data:
            name = app[0]
            n_reviews = float(app[3])
    
            if name in reviews_max and reviews_max[name] < n_reviews:
                reviews_max[name] = n_reviews
        
            elif name not in reviews_max:
                reviews_max[name] = n_reviews

        data_clean = []
        already_added = []

        for app in self.data:
            name = app[0]
            n_reviews = float(app[3])
    
            if (reviews_max[name] == n_reviews) and (name not in already_added):
                data_clean.append(app)
                already_added.append(name)
        self.data = data_clean
    
    def __is_english(self, string): 
         non_ascii = 0
         for character in string:
            if ord(character) > 127:
                non_ascii += 1
    
         if non_ascii > 3:
            return False
         else:
            return True
    
    def clean_english(self, index):
        data_english = []
        for app in self.data:
            name = app[index]
            if (self.__is_english(name)):
                data_english.append(app)
        self.data = data_english

    

    def remove_free_apps(self, index):
        data_final = []

        for app in self.data:
                price = app[index]
                if price == '0' or price == '0.0':
                    data_final.append(app)
        self.data = data_final
            
     
    
    def freq_table(self, index):
            table = {}
            total = 0
    
            for row in self.data:
                total += 1
                value = row[index]
                if value in table:
                    table[value] += 1
                else:
                    table[value] = 1
            
            table_percentages = {}
            for key in table:
                percentage = (table[key] / total) * 100
                table_percentages[key] = percentage 
            
            return table_percentages

    def display_table(self, index):
        table = self.freq_table(index)
        table_display = []
        for key in table:
            key_val_as_tuple = (table[key], key)
            table_display.append(key_val_as_tuple)
            
        table_sorted = sorted(table_display, reverse = True)
        for entry in table_sorted:
            print(entry[1], ':', entry[0])

        


    




       
