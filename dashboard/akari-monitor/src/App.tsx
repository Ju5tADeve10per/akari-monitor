import "./App.css";
import { useState, useEffect } from "react";

// Import Mock Data
import { mockClients } from "./mockData";

type Client = {
  last_timestamp: number;
  response: boolean;
};

type Clients = Record<string, Client>;

function App() {
  /* 下二行を切り替えてcssのテストを行う。*/
  // const [clients, setClients] = useState<Clients | null>(null);
  const [clients, setClients] = useState<Clients | null>(mockClients);

  async function fetchClients() {
    try {
      const res = await fetch("http://localhost:8000/clients");
      if (!res.ok) {
        throw new Error("HTTP error")
      }
      const data = await res.json();
      setClients(data);
    } catch (error) {
      if (error instanceof TypeError) {
        console.error("Network Error");
      }
      else {
        console.error(error)
      }
    }
  }

  useEffect(() => {
    fetchClients()

    const id = setInterval(fetchClients, 30000);

    return () => {
      clearInterval(id)
    }
  }, []);

  if (clients == null) {
    return (
      <main>
        <p>Loading...</p>
      </main>
    );
  }

  return (
    <main>
      {clients &&
        Object.entries(clients).map(([id, data]) => {
          return (
            <div key={id}>
              <p>{id}</p>
              <p>{data.last_timestamp}</p>
              <p>{data.response ? "OK" : "NG"}</p>
            </div>
          );
        })}
    </main>
  );
}

export default App;