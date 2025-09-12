# Dialogflow CX Python Client Example

This script demonstrates how to call the `detectIntent` method of the Dialogflow CX API using Python.

## Setup

### 1. Create a virtual environment

It is recommended to use a virtual environment to manage the dependencies for this project.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

Install the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3. Set up Google Cloud authentication

If you have not already done so, you will need to authenticate with Google Cloud.

*   Install the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install).
*   Run the following command to set up Application Default Credentials:

```bash
gcloud auth application-default login
```

### 4. Configure environment variables

This project uses a `.env` file to manage environment variables.

1.  Rename the `.env.example` file to `.env`.
2.  Open the `.env` file and replace the placeholder values with your actual Dialogflow agent information:

```
PROJECT_ID=your-google-cloud-project-id
LOCATION_ID=your-agent-location
AGENT_ID=your-agent-id
```

**Note:** The `SESSION_ID` is optional. If you do not provide one in the `.env` file, a random session ID will be generated for each run.

## Usage

Once you have completed the setup steps, you can run the script:

```bash
python dialogflow_client.py
```
