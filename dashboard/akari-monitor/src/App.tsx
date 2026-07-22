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
    const one = "Loading";
    const two = "Wait...";
    return (
      <main id="loading-container">
        <div className="scene">
          <div className="word">
            {one.split("").map((char, i) => (
              <span className="letter__wrap" key={i} style={{ animationDelay: `${i * 0.1}s`}}>
                <span className="letter">
                  <span className="letter__panel">{char}</span>
                  <span className="letter__panel">{two[i]}</span>
                  <span className="letter__panel">{char}</span>
                  <span className="letter__panel">{two[i]}</span>
                  <span className="letter__panel"></span>
                </span>
              </span>
            ))}
          </div>
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