import pcap_parser
import argparse, csv, os


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default="app_data/", type=str)
    parser.add_argument('--output', default="dataset.csv", type=str)
    result = parser.parse_args()
    print(result)

    input_folder = result.input
    output_file = result.output

    with open(output_file,'w') as f:
        writer = csv.writer(f)
        writer.writerow(pcap_parser.get_headers())

        class_lst = next(os.walk(input_folder))[1]
        print(class_lst)

        for cls in class_lst:
            sub_dir = os.path.join(input_folder, cls)
            print(sub_dir)
            for pcap_file in os.listdir(sub_dir):
                instance = pcap_parser.parse(os.path.join(sub_dir, pcap_file))
                if instance is not None:
                    instance = list(instance)
                    instance.append(cls)
                    writer.writerow(instance)


if __name__ == "__main__":
    main()