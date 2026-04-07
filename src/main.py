import sys
import os
import time
import matplotlib.pyplot as plt
from opt import parse_input, hvlcs

def get_graph_data(input, output):
    input_folder = input
    output_folder = output

    # create outputfolder if not created
    os.makedirs(output_folder, exist_ok=True)
    # create list of all folder names
    input_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".in")])

    runtimes = []
    lengths = []

    # run through each file in folder
    for file in input_files:
        path = os.path.join(input_folder, file)

        # read input
        try:
            k, alphabet, first_string, second_string = parse_input(path)
        except FileNotFoundError:
            print(f"Could not find {file}")
            continue
        
        lengths.append(len(first_string))
        
        # Run algorithm
        start_time = time.time()

        max_value, subsequence = hvlcs(first_string, second_string, alphabet)
        
        end_time = time.time()
        runtime = end_time - start_time
        runtimes.append(runtime)

        # Output info to console
        print(f"{file}")
        print(f"--------------")
        print(f"Max value = {max_value} \nSubsequence = {subsequence} \nRuntime = {runtime:.5f} seconds \n")

        # write .out file to data/graph/
        outfile_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.out")
        with open(outfile_path, 'w') as f:
            f.write(f"{max_value}\n{subsequence}\n")   
    

    runtimes_in_milliseconds = [r * 1000 for r in runtimes]

    file_labels = []
    for i in range(1, len(runtimes)+1):
        file_labels.append(f"ex{i}")

    # Plot graph with matplot
    plt.figure(figsize=(12,6))
    plt.plot(file_labels, runtimes_in_milliseconds, marker='o', linestyle='-', color='blue')

    # add in length of strings above points on graph
    for i, length in enumerate(lengths):
        plt.text(i, runtimes_in_milliseconds[i]+0.01, f"L={length}", ha='center', fontsize=8)

    plt.xlabel("Input File")
    plt.ylabel("Runtime (ms)")
    plt.title("HVLCS Runtime per Input File")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, "hvlcs_runtime.png"))
    plt.show()

def main():
    if len(sys.argv) <= 1:
        print("Please name a test file to run.")
        sys.exit(1)

    # batch run of files
    if (len(sys.argv) == 3):
        get_graph_data(sys.argv[1], sys.argv[2])
        return
    
    # single specified file
    file_path = sys.argv[1]
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    try:
        k, alphabet, first_string, second_string = parse_input(file_path)
    except FileNotFoundError:
        print(f"Could not find {file_name} within 'tests' folder")
        sys.exit(1)

    max_value, subsequence = hvlcs(first_string, second_string, alphabet)

    print(f"\n{file_name}.in")
    print(f"--------------")
    print(f"Max value = {max_value} \nSubsequence = {subsequence}\n")

    outfile = os.path.join("data", f"{file_name}.out")

    with open(outfile, 'w') as f:
        f.write(f"{max_value}\n")
        f.write(f"{subsequence}\n")


if __name__ == "__main__":
    main()