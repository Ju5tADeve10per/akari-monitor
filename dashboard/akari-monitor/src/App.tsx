import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [clients, setClients] = useState(null);

  async function fetchClients() {
    const res = await fetch("http://localhost:8000/clients");
    const data = await res.json();
    setClients(data);
  }

  useEffect(() => {
    // 後で定期実行の仕組みを書く。
    fetchClients();
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