from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import os
import json
import multiprocessing
from multiprocessing import Pool
import math

def setup_driver():
    """Setup Chrome driver with appropriate options for CI environment"""
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    return uc.Chrome(use_subprocess=True, options=chrome_options)

def test_number_range(args):
    """Test a range of numbers for valid promotion codes"""
    start, end, batch_id = args
    results = {
        'working': [],
        'failed': []
    }
    
    # Create a new driver instance for each process
    driver = setup_driver()
    wait = WebDriverWait(driver, 30)
    
    try:
        # Navigate to the page
        driver.get('https://www.etsy.com/uk/promotions')
        time.sleep(5)  # Initial load wait
        
        for number in range(start, end + 1):
            print(f'Process {batch_id} testing number: {number}')
            
            try:
                # Find and interact with elements
                input_field = wait.until(EC.presence_of_element_located((By.ID, 'input-promotion-code')))
                button = wait.until(EC.element_to_be_clickable((By.ID, 'button-redeem')))
                
                # Clear and enter number
                input_field.clear()
                input_field.send_keys(str(number))
                button.click()
                
                time.sleep(1)  # Wait for response
                
                # Check for error message
                try:
                    error_message = wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/form/div[2]/span')))
                    
                    if "Please enter a valid promotion code" in error_message.text:
                        print(f'❌ {number} failed: {error_message.text}')
                        results['failed'].append(number)
                        driver.refresh()
                        time.sleep(2)
                    else:
                        print(f'✅ {number} treated as success')
                        results['working'].append(number)
                        time.sleep(5)
                        driver.get('https://www.etsy.com/uk/promotions')
                except:
                    print(f'✅✅ {number} treated as success')
                    results['working'].append(number)
                    time.sleep(5)
                    driver.get('https://www.etsy.com/uk/promotions')
                    
            except Exception as e:
                print(f'Error processing number {number}: {str(e)}')
                results['failed'].append(number)
                driver.refresh()
                time.sleep(2)
                
    except Exception as e:
        print(f'Process {batch_id} encountered error: {str(e)}')
    finally:
        driver.quit()
        
    return results

def save_results(results, output_file='results.json'):
    """Save results to a JSON file"""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

def main(start_number=1051, end_number=1150, num_processes=4):
    """Main function to coordinate the testing processes"""
    # Calculate batch size for each process
    total_numbers = end_number - start_number + 1
    batch_size = math.ceil(total_numbers / num_processes)
    
    # Create batches for parallel processing
    batches = []
    for i in range(num_processes):
        batch_start = start_number + (i * batch_size)
        batch_end = min(batch_start + batch_size - 1, end_number)
        batches.append((batch_start, batch_end, i))
    
    # Initialize multiprocessing pool
    with Pool(processes=num_processes) as pool:
        results = pool.map(test_number_range, batches)
    
    # Combine results from all processes
    final_results = {
        'working': [],
        'failed': [],
        'metadata': {
            'start_number': start_number,
            'end_number': end_number,
            'total_tested': total_numbers,
            'processes_used': num_processes,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
    }
    
    for result in results:
        final_results['working'].extend(result['working'])
        final_results['failed'].extend(result['failed'])
    
    # Save results to file
    save_results(final_results)
    
    # Print final results
    print('=== Testing Complete ===')
    print('Working numbers:', final_results['working'])
    print('Total working numbers:', len(final_results['working']))
    print('Total tested numbers:', len(final_results['working']) + len(final_results['failed']))
    print(f'Results saved to {os.path.abspath("results.json")}')

if __name__ == '__main__':
    # Get parameters from environment variables or use defaults
    start_num = int(os.getenv('START_NUMBER', '1051'))
    end_num = int(os.getenv('END_NUMBER', '1150'))
    processes = int(os.getenv('NUM_PROCESSES', '4'))
    
    main(start_num, end_num, processes)
