import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
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

aisc_df = get_data()

with st.container():
    #shape filter container
    
    col1, col2, col3 = st.columns(3)

    with col1:
        unit_sys = st.selectbox("Unit System", ["US Customary", "Metric"])

    df = get_unit_system_data(aisc_df, unit_sys)

    with col2:
        shape_list = df.Type.unique().tolist()
        shape = st.selectbox("Shape Type", shape_list)

    df = df[df.Type==shape].dropna(axis=1)

    with col3:
        shape_name_list = df.AISC_Manual_Label.unique().tolist()[::-1]
        name = st.selectbox("Shape Name", shape_name_list)

    df = df[df.AISC_Manual_Label == name]

if shape == "W" or shape == "M" or shape == "HP":
    
    row_variables = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
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
        
    image = 'images/W.jpg'
    
    st.title('CROSS-SECTION')
    st.image(image, use_column_width='always')

    st.title('SECTION PROPERTIES')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header('Variable')
        for row in row_variables:
            st.markdown(row)
            
    with col2:
        st.header('Value')
        for row in row_values:
            st.markdown(df[row].values[0])
            
    with col3:
        st.header('Units')
        for row in shape_units:
            st.markdown(row)

if shape == "S":
    
    row_variables = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
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
        
    image = 'images/S.jpg'
    
    st.title('CROSS-SECTION')
    st.image(image, use_column_width='always')

    st.title('SECTION PROPERTIES')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header('Variable')
        for row in row_variables:
            st.markdown(row)
            
    with col2:
        st.header('Value')
        for row in row_values:
            st.markdown(df[row].values[0])
            
    with col3:
        st.header('Units')
        for row in shape_units:
            st.markdown(row)

if shape == "C" or shape == "MC":
    
    row_variables = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
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
        
    image = 'images/C.jpg'
    
    st.title('CROSS-SECTION')
    st.image(image, use_column_width='always')

    st.title('SECTION PROPERTIES')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header('Variable')
        for row in row_variables:
            st.markdown(row)
            
    with col2:
        st.header('Value')
        for row in row_values:
            st.markdown(df[row].values[0])
            
    with col3:
        st.header('Units')
        for row in shape_units:
            st.markdown(row)
            
if shape == "WT" or shape == "MT":
    
    row_variables = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
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
        
    image = 'images/WT.jpg'
    
    st.title('CROSS-SECTION')
    st.image(image, use_column_width='always')

    st.title('SECTION PROPERTIES')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header('Variable')
        for row in row_variables:
            st.markdown(row)
            
    with col2:
        st.header('Value')
        for row in row_values:
            st.markdown(df[row].values[0])
            
    with col3:
        st.header('Units')
        for row in shape_units:
            st.markdown(row)

if shape == "ST":
    
    row_variables = ['$W$ = ', '$A$ = ', '$d$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', 
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
        
    image = 'images/ST.jpg'
    
    st.title('CROSS-SECTION')
    st.image(image, use_column_width='always')

    st.title('SECTION PROPERTIES')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header('Variable')
        for row in row_variables:
            st.markdown(row)
            
    with col2:
        st.header('Value')
        for row in row_values:
            st.markdown(df[row].values[0])
            
    with col3:
        st.header('Units')
        for row in shape_units:
            st.markdown(row)
            
if shape == "HSS":
    
    row_variables = ['$W$ = ', '$A$ = ', '$H_t$ = ', '$b_f$ = ', '$t_w$ = ', '$t_f$ = ', '$T$ = ', 
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
        
    image = 'images/RecHSS.jpg'
    
    st.title('CROSS-SECTION')
    st.image(image, use_column_width='always')

    st.title('SECTION PROPERTIES')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header('Variable')
        for row in row_variables:
            st.markdown(row)
            
    with col2:
        st.header('Value')
        for row in row_values:
            st.markdown(df[row].values[0])
            
    with col3:
        st.header('Units')
        for row in shape_units:
            st.markdown(row)