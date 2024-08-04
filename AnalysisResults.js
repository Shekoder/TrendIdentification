import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AnalysisResults = () => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/analysis-results');
        setResults(response.data);
      } catch (err) {
        setError('Error fetching analysis results');
      } finally {
        setLoading(false);
      }
    };

    fetchResults();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h2>Analysis Results</h2>
      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
};

export default AnalysisResults;
