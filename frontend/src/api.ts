import axios from "axios";

export interface NodeDTO {
  id: number;
  key: string;
  label: string;
  description: string;
  url: string;
  category: string;
  parent: number | null;
  order: number;
}

export interface RoadmapDTO {
  id: number;
  slug: string;
  title: string;
  nodes: NodeDTO[];
}

export async function fetchRoadmap(slug: string): Promise<RoadmapDTO> {
  const res = await axios.get(`/roadmap/api/roadmaps/${slug}/`);
  return res.data;
}
