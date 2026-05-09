import subprocess
import os

def run_script(script_name):
    print(f"--- Executing: {script_name} ---")
    result = subprocess.run(['python', script_name], capture_output=True, text=True, encoding='utf-8')
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error in {script_name}:")
        print(result.stderr)

def main():
    scripts = [
        'main.py',
        'data_generator.py',
        'data_processor.py',
        'visualizer.py',
        'report_generator.py',
        'document_builder.py',
        'pdf_converter.py'
    ]
    
    print("=======================================")
    print("STARTING MARKETING ANALYTICS PIPELINE")
    print("=======================================")

    for script in scripts:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"File not found: {script}")

    print("=======================================")
    print("PIPELINE COMPLETE: Marketing Insights Ready.")
    print("Check 'outputs/' and 'figures/' folders.")
    print("=======================================")

if __name__ == "__main__":
    main()