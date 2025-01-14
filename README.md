# **Magic Math Setup Guide**

Follow these steps to clone the repository, set up the environment, and run the application:

### 1. Clone the Repository
```bash
git clone git@github.com:00suryavanshi00/magic_maths.git
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv assignmentvenv
source assignmentvenv/bin/activate
```

### 3. Navigate to the Project Directory
```bash
cd magic-math
```

### 4. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

---

### Access the Application

- **Base URL**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
  - Returns a welcome message: `{"message": "Hello Ctrl T"}`
  
- **Magic Math Endpoint**: [http://127.0.0.1:8000/magic_math/{N}](http://127.0.0.1:8000/magic_math/{N})
  - Replace `{N}` with a non-negative integer to calculate the result.
  - Example for \( N = 5 \):
    ```json
    {
        "N": 5,
        "magic_math": 26
    }
    ```

---

Enjoy exploring **Magic Math**! 🎉