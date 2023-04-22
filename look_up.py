####################
# By- Shreya Kapoor
####################

with open('mm_disease_out.out', 'r') as file:
    for line in file:
        data = line.strip().split('|')
        try:
            fourth_column_data = data[4]
        except IndexError:
            continue

        with open('disease_names_with_CUI', 'r') as lookup_file:
            for lookup_line in lookup_file:
                lookup_data = lookup_line.strip().split(',')
                try:
                    Ophthalmology_CUI_lookup = lookup_data[1]
                except IndexError:
                    continue

                if Ophthalmology_CUI_lookup == fourth_column_data:
                    with open('matching_rows.out', 'a') as output_file:
                        output_file.write(line)
                    break
