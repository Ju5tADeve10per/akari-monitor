import "./App.css";
import { useState, useEffect } from "react";

type Client = {
  last_timestamp: number;
  response: boolean;
};

type Clients = Record<string, Client>;

function App() {
  const [clients, setClients] = useState<Clients | null>(null);

  async function fetchClients() {
    // TODO: serverが落ちてる場合はそもそもfetchできないので、try, catchで捕まえる
    const res = await fetch("http://localhost:8000/clients");
    if (!res.ok) {
      console.error("Failed to fetch");
    }
    else {
      const data = await res.json();
      setClients(data);
    }
  }

  useEffect(() => {
    const id = setInterval(fetchClients, 30000);

    return () => {
      clearInterval(id)
    }
  }, []);

  if (clients == null) {
    // Loadingのことを書く。
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

// clients = {
//   client_id: {
//     "last_timestamp": int
//     "response": bool
//   }
// }