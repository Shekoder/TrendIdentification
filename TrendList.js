import React, { useEffect, useState } from 'react';

const TrendList = () => {
  const [trends, setTrends] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/trends')
      .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.text(); // Use text() to debug
      })
      .then(text => {
        try {
          const data = JSON.parse(text);
          setTrends(data);
        } catch (err) {
          setError('Invalid JSON format');
        }
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Trends</h1>
      <ul>
        {trends.map((trend, index) => (
          <li key={index}>{JSON.stringify(trend)}</li>
        ))}
      </ul>
    </div>
  );
};

export default TrendList;
