// App.tsx
import React, { useEffect, useState } from "react";

const App: React.FC = () => {
  const [message, setMessage] = useState("");
  console.log(process.env.REACT_APP_API_URL);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(process.env.REACT_APP_API_URL || "");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setMessage(data.message);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>ID Verification App</h1>
      <p>message: {message}</p>
    </div>
  );
};

export default App;
