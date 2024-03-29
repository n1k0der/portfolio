import streamlit as st 
import pandas as pd
from src.dataframe_class import dataframe


uploaded_file = st.file_uploader(label='Upload a csv, json or parquet file',
                                 type=['csv', 'json', 'parquet'])
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Dataframe', 
                            'Data Profiler',
                            'Modify Data', 
                            'Filter Data',
                            'Create Charts',
                            'Do you have an Excel file?'
                            ])

if uploaded_file is not None:
    if uploaded_file.name.endswith('csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('json'):
        df = pd.read_json(uploaded_file)
    elif uploaded_file.name.endswith('parquet'):
        df = pd.read_parquet(uploaded_file)
    else:
        print("ERROR: Not csv, json, parquet file provided an program pass")


with tab1:
    if uploaded_file is not None:
        st.dataframe(df)
with tab2:
    if uploaded_file is not None:
        data_profiler = dataframe.DataFrameGeneral(df)
        data_profiler.profiler_start()
        for key in data_profiler.profiler.keys():
            st.markdown(f'### {key}')
            final_text = ""
            col1, col2 = st.columns(2)
            if data_profiler.profiler[key].get('histogram') is not None:
                with col1:
                    st.plotly_chart(data_profiler.profiler[key]['histogram'])
            else:
                with col1:
                    st.markdown(f'# {data_profiler.profiler[key]['unique_values']}')
                    st.markdown(f'#### Unique Values')

            with col2:
                for k in data_profiler.profiler[key].keys():
                    if k != 'histogram':
                        final_text += f'**{k}:** {data_profiler.profiler[key][k]}  \n'
                    else:
                        continue
                st.write(final_text)
           
            # else:
            #     for k in data_profiler.profiler[key].keys():
            #         final_text += f'**{k}:** {data_profiler.profiler[key][k]}  \n'
            #     st.write(final_text)
            st.divider()