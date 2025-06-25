import pandas as pd
import os 
import glob

#way for read the files

folder_path = 'src\\data\\raw'

#for list all excel files

excel_files = glob.glob(os.path.join(folder_path , '*.xlsx'))

if not excel_files:
    print("nenhum arquivo excel encontrado")

else:
    
    #dataframe = for storage contet of files
    dfs = []
    for excel_file in excel_files:
        
        try:
            #read excel file
            df_temp = pd.read_excel(excel_file)

            #get files name
            file_name = os.path.basename(excel_file)
            
            df_temp['filename'] = file_name
            
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italia' in file_name.lower():
                df_temp['location'] = 'it'

            # A columm called campaign
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            
            #storage datas
            dfs.append(df_temp)
      

        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file} : {e}")

if dfs:
    #concatenate all tables saved in the fds into a single table
    result = pd.concat(dfs, ignore_index=True)
    #way to output
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')
    #config engine writer
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    result.to_excel(writer, index=False)

    writer._save()

else:
    print("no data to be saved")