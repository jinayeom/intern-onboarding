import { useEffect, useState } from "react";
import { fetchRoadmap, type RoadmapDTO, type NodeDTO } from "./api";

export default function App() {
  const [data, setData] = useState<RoadmapDTO | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchRoadmap("devops")
      .then(setData)
      .catch((err) => setError(String(err)))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!data) return <p>No roadmap found.</p>;

  return (
    <div style={{ padding: "2rem" }}>
      <h1>{data.title}</h1>
      <ul>
        {data.nodes.map((node) => (
          <li key={node.id}>
            <button onClick={() => (window.location.href = `/tutorials/${node.key}/`)}>
              {node.label}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
