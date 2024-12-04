import { Author } from "./Author";

export interface Book {
    id: number;
    name: string;
    authors: Author[];
    year: number;
}

export interface BookCreateDto{
  name: string,
  authorIds: number[],
  year: number
}

export interface BookUpdateDto{
  name?: string,
  authorIds?: number[],
  year?: number
}