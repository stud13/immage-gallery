import React from 'react';
import { Button } from 'react-bootstrap';

const Welcome = () => (
  <div className="containerFluid py-5" style={{ backgroundColor: 'lightgrey' }}>
    <div style={{ padding: 10 }}>
      <h1>Images Gallery</h1>
      <p>
        This is simple application that retrieves photos using Unsplash API. In
        order to start enter search term in the input field.
      </p>
      <p>
        <Button variant="primary" href="https://unsplash.com" target="_blank">
          Check
        </Button>
      </p>
    </div>
  </div>
);

export default Welcome;
