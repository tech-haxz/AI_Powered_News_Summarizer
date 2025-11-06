import { useState } from "react";
import axios from "axios";
import "./Summarizer.css";

const Summarizer = () => {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState(null);

  const handleSummarize = async () => {
    if (!url.trim()) {
      setError("Please enter a valid news URL.");
      return;
    }

    setLoading(true);
    setError(null);
    setSummary(null);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/v1/summarize/", {
        url,
      });

      setSummary(response.data);

      console.log(summary.summary);
    } catch (err) {
      setError("Failed to summarize. Check your backend or URL.");
    } finally {
      setLoading(false);
    }
  };

  

  return (
    <div className="summarizer-container">
      <h1>🧠 AI News Summarizer</h1>
      <p className="subtitle">Summarize any news article in seconds!</p>

      <div className="input-box">
        <input
          type="text"
          placeholder="Enter news article URL..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={handleSummarize} disabled={loading}>
          {loading ? "Summarizing..." : "Summarize"}
        </button>
      </div>

      {/* {error && <p className="error">{error}</p>} */}

      {summary && (
        <div className="result-box">
          <h2>{summary.title}</h2>
          <p>{summary.summary}</p>
        </div>
      )}
    </div>
  );
};

export default Summarizer;
