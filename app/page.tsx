// app/page.tsx
import React from 'react';

export default function HomePage() {
  return (
    <div>
      <section className="hero">
        <div className="container">
          <h1>Start mining and get your (simulated) profit today!</h1>
          <p>This is a research project simulating a cloud mining platform.</p>
          <button>Start Mining (Simulation)</button>
        </div>
      </section>
      {/* Other content can go here */}
    </div>
  );
}
