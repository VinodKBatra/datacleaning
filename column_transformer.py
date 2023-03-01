#!/usr/bin/env python
# coding: utf-8

# In[45]:


## @author Vinod Batra

class Column_transformer:
    
    def __init__(self, df):
        
        self.df = df
        self.col_dict = {}
               
    
    def _set_column_dict(self):
        
        binary_cat_columns, multiple_cat_columns, numerical_columns = [], [], []
        column_dict = {}
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
            
                if self.df[col].nunique() == 2:
                    binary_cat_columns.append(self.df[col].name)
                else:
                    multiple_cat_columns.append(self.df[col].name)
        
            elif self.df[col].dtype == 'bool':
                binary_cat_columns.append(self.df[col].name)
        
            else:
                numerical_columns.append(self.df[col].name)
    
        column_dict['binary_cat_columns'] = binary_cat_columns
        column_dict['multiple_cat_columns'] = multiple_cat_columns
        column_dict['numerical_columns'] = numerical_columns

        return column_dict
     
    def get_column_types(self):        
        
        '''returns the categorized columns as a dictionary'''
        
        return self._set_column_dict()
    
    def get_selected_columns(self, column = 'binary_cat_columns'):
        
        '''returns the dictionary values of the column as a list
        '''
        return self._set_column_dict()[column]
         
   
    def binary_categorical_to_numerical(self):
    
        '''Converts binary categorical columns to numerical columns of a dataframe 
        RETURNS
            modiffied dataframe'''
        col_names = self.get_selected_columns()
        
        for col_name in col_names:
            self.df[col_name] = self.df[col_name].replace(self.df[col_name].unique()[0], '0')
            self.df[col_name] = self.df[col_name].replace(self.df[col_name].unique()[1], '1')
            self.df[col_name] = self.df[col_name].astype('uint8')
        
        return self.df





