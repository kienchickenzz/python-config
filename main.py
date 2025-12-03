import os

from config import Config

# Quick test
if __name__ == "__main__":
    # Test 1: Biến môi trường
    os.environ["APP_NAME"] = "TestApp"
    os.environ["DEBUG"] = "true"
    os.environ["PORT"] = "3000"
    
    config = Config()
    
    print("=== Quick Test ===")
    print(f"App Name: {config.get_config('APP_NAME', 'Default')}")
    print(f"Debug Mode: {config.get_bool('DEBUG', False)}")
    print(f"Port: {config.get_int('PORT', 8080)}")
    
    # Test 2: Custom config
    custom = Config({
        "API_KEY": "abc123",
        "MAX_USERS": "100",
        "FEATURES": "auth,profile,chat"
    })
    
    print(f"\nAPI Key: {custom.require_config('API_KEY')}")
    print(f"Max Users: {custom.require_int('MAX_USERS')}")
    print(f"Features: {custom.require_list('FEATURES', ',')}")
    
    # Test 3: Error cases
    print("\n=== Error Tests ===")
    try:
        config.require_config("NON_EXISTENT")
    except Exception as e:
        print(f"Missing config error: {type(e).__name__}: {e}")
    