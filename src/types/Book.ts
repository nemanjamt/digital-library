import { Author } from "./Author";

export interface Book {
    id: string;
    name: string;
    authors: Author[];
    year: number;
  }