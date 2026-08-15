import "./App.css";
import { useState, useEffect } from "react";

type Client = {
  last_timestamp: number;
  response: boolean;
};

type Clients = Record<string, Client>;

/**
 * This is the main function that is called by itself.
 * 
 * Display all current clients data according to the specific format.
 * 
 * @returns void
 */
function App() {
  /* When App is called by itself, useState is always executed first as a init trigger. */
  const [clients, setClients] = useState<Clients | null>(null);

  /**
   * Access to the server to get client list
   * 
   * Fetch the URL to get client list, if it failed, display the errors according to the error type.
   * 
   * @returns void
   */
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

  /* Call fetchClients() every 5 seconds */
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