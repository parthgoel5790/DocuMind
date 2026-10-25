import os
from models import TextDocument, CodeDocument
from engine import IntelligenceSystem

def main():
    system = IntelligenceSystem()
    while True:
        print("\n" + "="*45)
        print("    DOCUMIND: LOCAL AUTOMATED DATA ENGINE    ")
        print("="*45)
        print("1. 📁 Scan & Register a New File")
        print("2. 📊 View Analyzed Documents & Metrics")
        print("3. 🔍 Search Keyword Across Files (Search Engine)")
        print("4. ❌ Exit Application")
        print("="*45)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            file_path = input("\nEnter the file path or name (e.g., test.txt): ").strip()
            if not os.path.exists(file_path):
                print("❌ File does not exist! Please check the file name and path.")
                continue
            
            if file_path.endswith('.py'):
                doc = CodeDocument(file_path, "code")
                system.add_document(doc)
                print(f"✅ Registered '{file_path}' as a Code Framework module.")
            else:
                doc = TextDocument(file_path, "text")
                system.add_document(doc)
                print(f"✅ Registered '{file_path}' as an Analytical Text document.")
                
        elif choice == "2":
            if not system.control:
                print("\n⚠️ No documents indexed yet.")
                continue
                
            print("\n--- INDEXED RECORDS & ARCHITECTURE INSIGHTS ---")
            for filename, doc_obj in system.control.items():
                print(f"\n📄 File: [ {filename} ] | Type: {doc_obj.file_type.upper()}")
                if doc_obj.file_type == "text":
                    metrics = doc_obj.get_metrics()
                    for key, val in metrics.items():
                        print(f"   -> {key}: {val}")
                elif doc_obj.file_type == "code":
                    structure = doc_obj.parse_code()
                    print(f"   -> Found Classes  : {structure['classes']}")
                    print(f"   -> Found Functions: {structure['functions']}")
                    
        elif choice == "3":
            keyword = input("\nEnter search token or string: ").strip()
            if not keyword:
                print("⚠️ Search input cannot be empty.")
                continue
                
            results = system.search_keyword(keyword)
            print(f"\n🔍 Query Matches for '{keyword}':")
            if not results:
                print("   No instances found across the directory structure.")
            else:
                for file, lines in results.items():
                    print(f"   📍 File '{file}' -> Matches on Line(s): {lines}")
                    
        elif choice == "4":
            print("\nExiting System. Keep Coding! 🚀")
            break
        else:
            print("❌ Invalid Option selected. Choose between 1 and 4.")

if __name__ == "__main__":
    main()
