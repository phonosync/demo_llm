import glob

def combine_text_files(output_file):
    # Get a list of all txt files in the input folder
    txt_files = glob.glob('*.txt')
    
    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate through each txt file
        for txt_file in txt_files:
            # Open the txt file in read mode
            with open(txt_file, 'r') as infile:
                # Read the contents of the file and write to the output file
                outfile.write(infile.read())
                # Optionally add a newline character to separate contents of different files
                outfile.write('\n')

output_file = 'shakespeare_deutsch_komplett.txt'  # Replace with your desired output file name

combine_text_files(output_file)
