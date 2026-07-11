import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [clients, setClients] = useState(null);

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
      <h1>Akari Monitor</h1>
    </main>
  );
}

export default App;