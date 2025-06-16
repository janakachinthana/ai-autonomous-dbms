# Intelligent Indexing Module Entry Point
from index_manager import IndexManager
import time

def main():
    print("Starting Intelligent Indexing Module...")
    manager = IndexManager()
    for _ in range(3):
        column = manager.monitor_access()
        recommendation = manager.recommend_index(column)
        print(f"Accessed: {column}\nRecommendation: {recommendation}")
        if 'CREATE INDEX' in recommendation:
            result = manager.apply_index(column)
            print(f"Action: {result}\n")
        else:
            print()
        time.sleep(1)

if __name__ == "__main__":
    main()
