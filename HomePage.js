import React from 'react';
import TrendList from '../components/TrendList';
import AnalysisResults from '../components/AnalysisResults';

const HomePage = () => {
  return (
    <div>
      <h1>Trend Identification System</h1>
      <TrendList />
      <AnalysisResults />
    </div>
  );
};

export default HomePage;
