import psutil

def main():
    data = psutil.cpu_count()
    datamem = psutil.virtual_memory()
    print(data, "\n", datamem)



if __name__ == "__main__":
    main()
