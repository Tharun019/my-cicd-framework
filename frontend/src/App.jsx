// App.jsx
// Main component — what users see in the browser
import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [backendMessage, setBackendMessage] = useState("Loading...");
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    fetch("/api/hello")
      .then((response) => response.json())
      .then((data) => {
        setBackendMessage(data.message);
        setStatus("Connected ✅");
      })
      .catch((error) => {
        setBackendMessage("Could not reach backend");
        setStatus("Not Connected ❌");
      });
  }, []);

  return (
    <div className="app">
      <header className="header">
        <h1>🚀 My CI/CD Framework</h1>
        <p>Built with React + FastAPI + Docker + GitHub Actions</p>
      </header>

      <div className="card">
        <h2>Pipeline Stages</h2>
        <div className="stages">
          <div className="stage">✅ Code Pushed to GitHub</div>
          <div className="stage">✅ GitHub Actions Triggered</div>
          <div className="stage">✅ Frontend Built (React)</div>
          <div className="stage">✅ Backend Built (FastAPI)</div>
          <div className="stage">✅ Tests Passed</div>
          <div className="stage">✅ Docker Container Running</div>
          <div className="stage">✅ App Deployed</div>
        </div>
      </div>

      <div className="card">
        <h2>Backend Connection</h2>
        <p>
          Status: <strong>{status}</strong>
        </p>
        <p>
          Message from FastAPI: <strong>{backendMessage}</strong>
        </p>
      </div>

      <div className="card">
        <h2>What is Running</h2>
        <p>🌐 Frontend → React (Port 3000)</p>
        <p>⚙️ Backend → FastAPI (Port 8000)</p>
        <p>🐳 Container → Docker</p>
        <p>🔄 Pipeline → GitHub Actions</p>
      </div>
    </div>
  );
}

export default App;
