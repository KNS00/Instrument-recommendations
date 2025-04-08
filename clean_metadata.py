def main():
    with open('metadata.tsv', 'r') as file:
        lines = file.readlines()

    # We simply just replace tabs. This has NO effect on the preprocessing, it was just because for some reason I was not able to load it.
    cleaned_lines = []
    for line in lines:
        fields = line.strip().split('\t')
        if len(fields) > 3:  
            item_id = fields[0]
            title = fields[1]
            description = ' '.join(fields[2:])  
            cleaned_line = f"{item_id}\t{title}\t{description}\n"
            cleaned_lines.append(cleaned_line)
        else:
            cleaned_lines.append(line)

    with open('metadata_cleaned.tsv', 'w') as file:
        file.writelines(cleaned_lines)
    
if __name__=="__main__":
    main()
