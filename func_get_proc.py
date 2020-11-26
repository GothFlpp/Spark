def get_proc(df_app, merge_fields, tabela_synapse, tabela_stg_synapse):
    
    
    proc_update = "UPDATE TARGET\nSET\n"
    
    for field in df_app.columns:
      proc_update += (f"TARGET.{field} = SOURCE.{field},\n")
    
    proc_update = proc_update[:-2]
    proc_update += ("\n\n")
    proc_update += (f"FROM {tabela_synapse} AS TARGET\n")
    proc_update += (f"INNER JOIN {tabela_stg_synapse} AS SOURCE\n") 
    proc_update += (f"ON ") 
    
    for field in merge_fields:
      proc_update += (f"TARGET.{field} = SOURCE.{field} AND\n")
    
    proc_update = proc_update[:-5]
    proc_update += ";\n\n"
    
    #print(proc_update)
    
    
    proc_insert = f"INSERT INTO {tabela_synapse}\nSELECT\n"
    for field in df_app.columns:
      proc_insert += (f"SOURCE.{field},\n")
    
    proc_insert = proc_insert[:-2]
    proc_insert += ("\n\n")
    proc_insert += (f"FROM {tabela_stg_synapse} AS SOURCE\n")
    proc_insert += ("WHERE NOT EXISTS\n(\nSELECT 1\n")
    proc_insert += (f"FROM {tabela_synapse}\nWHERE ")
    
    for field in merge_fields:
      proc_insert += (f"{field} = SOURCE.{field} AND\n")
    
    proc_insert = proc_insert[:-5]
    proc_insert += ");"
    
    #print(proc_insert)
    
    
    proc = proc_update + proc_insert
    
    print(proc)
    return proc 