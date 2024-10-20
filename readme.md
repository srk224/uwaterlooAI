# 🚀 UwaterlooAI

**UwaterlooAI** is an AI-powered assistant designed to provide seamless access to University of Waterloo's course, location, and service information. With a sleek user interface and a powerful backend, UwaterlooAI leverages modern cloud technology to deliver information in real-time. Whether you’re a student searching for dining options or looking for course schedules, UwaterlooAI has you covered!


[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]() [![License](https://img.shields.io/github/license/your-repo/UwaterlooAI.svg)]() [![Vercel](https://vercelbadge.vercel.app/api/your-vercel-url)]()

## 🌟 Features

- 🧠 **AI-Powered Responses**: Get precise answers to your queries about the University of Waterloo's services, dining options, and more.
- 🌐 **Cloud-Integrated**: Hosted on [Vercel](https://vercel.com), making it fast, scalable, and reliable.
- 📅 **Real-Time Data**: Access up-to-date course schedules, dining hours, and building locations.
- 🎨 **User-Friendly Interface**: A modern and responsive frontend with a clean, minimalistic design.
- ⚙️ **Fully Automated CI/CD Pipeline**: Uses Jenkins for automated testing and deployment, ensuring a smooth development workflow.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

### Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/)
- [Vercel CLI](https://vercel.com/docs/cli)
- [Jenkins](https://www.jenkins.io/)

### 🔧 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/UwaterlooAI.git
   cd UwaterlooAI
Set up a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Install the Vercel CLI (if not already installed):

bash
Copy code
npm install -g vercel
Deploy the frontend:

bash
Copy code
vercel
Follow the prompts to deploy the frontend on Vercel.

Run the Flask backend locally:

bash
Copy code
python app.py
The backend should now be running at http://localhost:5000.

🌐 Deployment with Jenkins
Configure Jenkins to automate deployments:

Add your Vercel Token as a Jenkins credential.
Set up a Pipeline Job with the provided Jenkinsfile.
Trigger the job manually or set up GitHub webhooks for automatic deployment.
Monitor the deployment via the Jenkins console and the Vercel dashboard.

📚 API Endpoints
/query: Takes a user query and returns the response based on available University of Waterloo data.
/v3/FoodServices/outlets: Provides information on all dining options, including hours and locations.
/v3/Locations: Returns details about various campus buildings and services.
🎨 Frontend Preview
Here's a sneak peek of the user interface:

<!-- Replace with actual screenshot URL -->

The user interface is designed to be minimal and user-friendly, allowing you to interact with UwaterlooAI effortlessly.

💡 How It Works
User Input: Enter your query (e.g., "What dining options are open today?") in the input field.
Backend Processing: The Flask backend processes the request and queries the University of Waterloo API.
AI-Powered Response: The response is processed using AI to extract and present the most relevant information.
Frontend Display: The result is displayed neatly in the user interface, making it easy for users to understand.
📂 Project Structure
php
Copy code
UwaterlooAI/
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── vercel.json          # Vercel deployment configuration
├── Jenkinsfile          # Jenkins pipeline configuration
├── static/              # Static assets (HTML, CSS, JS)
├── templates/           # HTML templates for the Flask app
└── README.md            # This README file
🛠️ Built With
Python - Backend programming language
Flask - Python web framework
Vercel - Hosting and deployment platform for the frontend
Jenkins - Continuous Integration and Deployment
JavaScript/HTML/CSS - Frontend technologies for a sleek UI
🧑‍💻 Contributing
Contributions are what make the open-source community such an amazing place to be, learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
📝 License
Distributed under the MIT License. See LICENSE for more information.

❤️ Acknowledgements
Vercel for hosting and deployment.
University of Waterloo Open Data API for providing campus information.
Jenkins for making CI/CD a breeze.
📬 Contact
Your Name - your-email@example.com

Project Link: https://github.com/your-username/UwaterlooAI