import os
import sys


if __name__ == '__main__':
    print("Number of arguments:", len(sys.argv), "arguments")
    print("Argument List:", str(sys.argv))
    if len(sys.argv) > 2:
        index_path = sys.argv[1]
        bloom_filename = sys.argv[2]
        data = []
        buckets_cnt = 0
        for root, subdirs, files in os.walk(index_path):
            for d in subdirs:
                path = os.path.join(root, d, bloom_filename)
                if not os.path.exists(path):
                    data.append(d)
                buckets_cnt += 1
        print(f"Totally index contains {buckets_cnt} buckets")
        if len(data) > 0:
            print(f"Found {len(data)} buckets without {bloom_filename} file:")
            for d in data:
                print('\t', d)
        else:
            print("Index is OK")
    else:
        print("Error. Index path or filename is absent. Set args as <index-path> <filename>")