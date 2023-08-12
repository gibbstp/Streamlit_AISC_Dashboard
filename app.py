import pandas as pd
import streamlit as st

@st.cache_data
def read_data():
    return pd.read_csv("data/database.csv", sep=",", na_values="NaN")
    
@st.cache_data
def get_unit_system_data(dataframe, unit_system):
    """
    Selects shape values for each unit system.
    Two possible systems are US Customary and Metric
    
    Input:
    df (pd dataframe): Pandas dataframe of shapes database
    system (str): desired unit system
    
    Returns:
    df (pd dataframe): Pandas dataframe of desired unit system
    """
    
    if unit_system == "US Customary":
        df_unit_system = dataframe.loc[:,:"EDI_Std_Nomenclature.1"]

        
    else:
        df_unit_system = dataframe.loc[:,"EDI_Std_Nomenclature.1":]
        #removing ".1" from column names
        df_unit_system.columns = [column[:-2] for column in list(df_unit_system.columns)]
        #adding shape type back into dataframe
        df_unit_system["Type"] = dataframe["Type"]
        
    return df_unit_system

@st.cache_data
def get_shape_type_list(dataframe):
    '''
    Gets uique shape types
    
    '''
    
    return dataframe.Type.unique().tolist()

@st.cache_data
def get_shape_name_list(dataframe, shape: str):
    '''
    Gets unique shapes names and orders them in ascending order
    
    return: list
    '''
    
    return dataframe.AISC_Manual_Label.unique().tolist()[::-1]

@st.cache_data
def get_shape_rows(shape: str, unit_sys: str) -> list:
    '''
    TODO: add L type
    TODO: add 2L type
    TODO: add round hss type
    TODO: add pipe type
    
    Creates list of lists that contains shape information.
    Contains:
    1. shape variable lable
    2. shape variable value
    3. shape varaiable unit
    4. shape image
    
    returns:
    list of list
    
    '''
    
    if shape == "W" or shape == "M" or shape == "HP":
    
        row_labels = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
                        '$k_{des}$ = ', '$k_1$ = ', '$I_x$ = ', '$Z_x$ = ', '$S_x$ = ', '$r_x$ = ',
                        '$I_y$ = ', '$Z_y$ = ', '$S_y$ = ', '$r_y$ = ']

        row_values = ['W', 'A', 'd', 'bf', 'tw', 'tf', 'T', 'kdes', 'k1', 'Ix', 'Zx', 'Sx', 'rx', 
                    'Iy', 'Zy', 'Sy', 'ry']
        
        if unit_sys == "US Customary":                
            shape_units = ['lb/ft', 'in$^2$', 'in.', 'in.', 'in.', 'in.', 'in.', 'in.', 'in.',
                        'in$^3$', 'in$^3$', 'in$^3$', 'in.', 'in$^3$', 'in$^3$', 'in$^3$', 'in.']
        else:               
            shape_units = ['kg/m', 'mm$^2$', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.',
                        'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.', 'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.']
        
    elif shape == "S":
    
        row_labels = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
                        '$k_{des}$ = ', '$I_x$ = ', '$Z_x$ = ', '$S_x$ = ', '$r_x$ = ',
                        '$I_y$ = ', '$Z_y$ = ', '$S_y$ = ', '$r_y$ = ']

        row_values = ['W', 'A', 'd', 'bf', 'tw', 'tf', 'T', 'kdes', 'Ix', 'Zx', 'Sx', 'rx', 
                    'Iy', 'Zy', 'Sy', 'ry']
        
        if unit_sys == "US Customary":                
            shape_units = ['lb/ft', 'in$^2$', 'in.', 'in.', 'in.', 'in.', 'in.', 'in.',
                        'in$^3$', 'in$^3$', 'in$^3$', 'in.', 'in$^3$', 'in$^3$', 'in$^3$', 'in.']
        else:               
            shape_units = ['kg/m', 'mm$^2$', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.',
                        'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.', 'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.']
    
    elif shape == "C" or shape == "MC":
        
        row_labels = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
                        '$k_{des}$ = ', '$I_x$ = ', '$Z_x$ = ', '$S_x$ = ', '$r_x$ = ',
                        '$I_y$ = ', '$Z_y$ = ', '$S_y$ = ', '$r_y$ = ']

        row_values = ['W', 'A', 'd', 'bf', 'tw', 'tf', 'T', 'kdes', 'Ix', 'Zx', 'Sx', 'rx', 
                    'Iy', 'Zy', 'Sy', 'ry']
        
        if unit_sys == "US Customary":                
            shape_units = ['lb/ft', 'in$^2$', 'in.', 'in.', 'in.', 'in.', 'in.', 'in.',
                        'in$^3$', 'in$^3$', 'in$^3$', 'in.', 'in$^3$', 'in$^3$', 'in$^3$', 'in.']
        else:               
            shape_units = ['kg/m', 'mm$^2$', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.',
                        'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.', 'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.']
    
    elif shape == "WT" or shape == "MT":
    
        row_labels = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
                        '$k_{des}$ = ', '$I_x$ = ', '$Z_x$ = ', '$S_x$ = ', '$r_x$ = ',
                        '$I_y$ = ', '$Z_y$ = ', '$S_y$ = ', '$r_y$ = ']

        row_values = ['W', 'A', 'd', 'bf', 'tw', 'tf', 'T', 'kdes', 'Ix', 'Zx', 'Sx', 'rx', 
                    'Iy', 'Zy', 'Sy', 'ry']
        
        if unit_sys == "US Customary":                
            shape_units = ['lb/ft', 'in$^2$', 'in.', 'in.', 'in.', 'in.', 'in.', 'in.',
                        'in$^3$', 'in$^3$', 'in$^3$', 'in.', 'in$^3$', 'in$^3$', 'in$^3$', 'in.']
        else:               
            shape_units = ['kg/m', 'mm$^2$', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.',
                        'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.', 'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.']
        
    elif shape == "ST":
        
        row_labels = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', 
                        '$k_{des}$ = ', '$I_x$ = ', '$Z_x$ = ', '$S_x$ = ', '$r_x$ = ',
                        '$I_y$ = ', '$Z_y$ = ', '$S_y$ = ', '$r_y$ = ']

        row_values = ['W', 'A', 'd', 'bf', 'tw', 'tf', 'kdes', 'Ix', 'Zx', 'Sx', 'rx', 
                    'Iy', 'Zy', 'Sy', 'ry']
        
        if unit_sys == "US Customary":                
            shape_units = ['lb/ft', 'in$^2$', 'in.', 'in.', 'in.', 'in.', 'in.',
                        'in$^3$', 'in$^3$', 'in$^3$', 'in.', 'in$^3$', 'in$^3$', 'in$^3$', 'in.']
        else:               
            shape_units = ['kg/m', 'mm$^2$', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.',
                        'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.', 'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.']
        
    elif shape == "RECT HSS": #FIXME: correct hss information
    
        row_labels = ['$W$ = ', '$A$ = ', '$H_t$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
                        '$k_{des}$ = ', '$I_x$ = ', '$Z_x$ = ', '$S_x$ = ', '$r_x$ = ',
                        '$I_y$ = ', '$Z_y$ = ', '$S_y$ = ', '$r_y$ = ']

        row_values = ['W', 'A', 'Ht', 'bf', 'tw', 'tf', 'T', 'kdes', 'Ix', 'Zx', 'Sx', 'rx', 
                    'Iy', 'Zy', 'Sy', 'ry']
        
        if unit_sys == "US Customary":                
            shape_units = ['lb/ft', 'in$^2$', 'in.', 'in.', 'in.', 'in.', 'in.', 'in.',
                        'in$^3$', 'in$^3$', 'in$^3$', 'in.', 'in$^3$', 'in$^3$', 'in$^3$', 'in.']
        else:               
            shape_units = ['kg/m', 'mm$^2$', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.', 'mm.',
                        'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.', 'mm$^3$', 'mm$^3$', 'mm$^3$', 'mm.']
        
    rows = [[label, value, unit] for label, value, unit in zip(row_labels, row_values, shape_units)]
    
    return rows

@st.cache_data
def get_shape_image(shape: str):
    '''
    TODO: add round hss image
    
    Returns shape image path
    
    returns: relative path string    
    '''
    
    if shape == "W" or shape == "M" or shape == "HP":
        image_path = 'images/W.jpg'
        
    elif shape == "S":
        image_path = 'images/S.jpg'
    
    elif shape == "C" or shape == "MC":
        image_path = 'images/C.jpg'
    
    elif shape == "WT" or shape == "MT":
        image_path = 'images/WT.jpg'
        
    elif shape == "ST":
        image_path = 'images/ST.jpg'
        
    elif shape == "RECT HSS":
        image_path = 'images/RectHSS.jpg'
    
    return image_path
 
    ####################################################################################################

aisc_df = read_data()

with st.container():
    #shape filter container
    
    col1, col2, col3 = st.columns(3)

    with col1:
        unit_sys = st.selectbox("Unit System", ["US Customary", "Metric"])

    df = get_unit_system_data(aisc_df, unit_sys)

    with col2:
        shape_list = get_shape_type_list(df) 
        shape = st.selectbox("Shape Type", shape_list)

    #selecting desired shape list and dropping empty columns
    df = df[df.Type==shape].dropna(axis=1)

    with col3:
        #getting list of unique column names of dataframe and ordering in ascending order
        shape_name_list = get_shape_name_list(df, shape)
        name = st.selectbox("Shape Name", shape_name_list)

    df = df[df.AISC_Manual_Label == name]


with st.container():
    #shape information container
    
    st.title('CROSS-SECTION')
    st.image(get_shape_image(shape), use_column_width='always')
    st.title('SECTION PROPERTIES')
    
    col1, col2, col3 = st.columns(3)
    col1.header("Variable")
    col2.header("Value")
    col3.header("Units")
    
    shape_rows = get_shape_rows(shape, unit_sys)
    
    for shape_row in shape_rows:
        label, variable, unit = shape_row        
        col1.markdown(label)
        col2.markdown(df[variable].values[0])
        col3.markdown(unit)