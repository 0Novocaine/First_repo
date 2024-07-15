from functions import *
from decorators import *


@validate_log_level
def main():
    if len(sys.argv) < 2:
        print("Использование: python main.py path/to/logfile.log log_level")
        sys.exit(1)
    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None
    logs = load_logs(file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    if log_level:
        filtered_messages = filter_logs_by_level(logs, log_level)
        display_filtered_logs(filtered_messages, log_level)

if __name__ == "__main__":
    main()

