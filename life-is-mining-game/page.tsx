// app/page.tsx
import React from 'react';

export default function HomePage() {
  return (
    <div>
      <section className="hero">
        <div className="container">
          <div className="stat_hero"> {/* Start of stat_hero */}
            <div className="block_stat">
              <img src="/invested.svg" alt="Invested" /> {/* Local image path */}
              <h4>7.6m</h4>
              <span>Invested</span>
            </div>
            <div className="block_stat">
              <img src="/paid.svg" alt="Paid Out" /> {/* Local image path */}
              <h4>2.1m</h4>
              <span>Paid out</span>
            </div>
            <div className="block_stat">
              <img src="/users.svg" alt="Users" /> {/* Local image path */}
              <h4>1.2m</h4>
              <span>Users</span>
            </div>
          </div> {/* End of stat_hero */}

          <p>
            Mining is one of the leading cryptocurrency mining platforms. No need to purchase hardware devices, manage devices, offering cryptocurrency mining capacities in every range - for newcomers. (This is a simulation)
          </p>
          <button>Start mining (Simulation)</button>

          {/* Hero image (add later) */}
          {/* <div className="image_hero">
            <img src="/hero_img.png" alt="Hero Image" className="img-fluid" />
          </div> */}

        </div>
      </section>
      {/* Other content can go here */}
    </div>
  );
      }
