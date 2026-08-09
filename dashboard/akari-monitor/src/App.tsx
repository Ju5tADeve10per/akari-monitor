import "./App.css";
import { useState, useEffect } from "react";

// Import Mock Data
// import { mockClients } from "./mockData";

type Client = {
  last_timestamp: number;
  response: boolean;
};

type Clients = Record<string, Client>;

function App() {
  /* 下二行を切り替えてcssのテストを行う。*/
  const [clients, setClients] = useState<Clients | null>(null);
  // const [clients, setClients] = useState<Clients | null>(mockClients);

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
        console.error(error);
      }

      setClients(null);
    }
  }

  useEffect(() => {
    fetchClients()

    const id = setInterval(fetchClients, 5000);

    return () => {
      clearInterval(id)
    }
  }, []);

  if (clients == null) {
    return (
      <main className="loading-container">
        <div className="loading">
          {"Now Loading".split("").map((char, i) => (
            <span key={i} style={{ animationDelay: `${i * 0.1}s`}}>{char}</span>
          ))}
        </div>
      </main>
    );
  }

  return (
    <main id="client-dashboard">
      <div className="header">
        <p>Client ID</p>
        <p>Last Heartbeat</p>
        <p>Alive Status</p>
      </div>
      {clients &&
        Object.entries(clients).map(([id, data]) => {
          return (
            <div key={id}>
              <p className="client_id">{id}</p>
              <p className="timestamp">{new Date(data.last_timestamp * 1000).toLocaleString("ja-JP")}</p>
              <p className={data.response ? "ok" : "ng"}>{data.response ? "SUCCESS" : "FAILURE"}</p>
            </div>
          );
        })}
    </main>
  );
}

export default App;