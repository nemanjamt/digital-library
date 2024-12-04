import { Request, Response } from "express";
import { Book, BookCreateDto, BookUpdateDto } from "../types/Book";
import { Author } from "../types/Author";
import { authors } from "./authorController";

let books: Book[] = [];

export const getAllBooks = (req: Request, res: Response) => {
    res.json(books);
};

export const getBookById = (req: Request, res: Response) => {
  const id: number = Number(req.params.id); // Konverzija u broj
  
  if (isNaN(id)) {
      return res.status(400).send("Invalid ID format");
  }
  
    const book = books.find(b => b.id === id);
    if (!book) return res.status(404).send("Book not found");
    res.json(book);
};

export const createBook = (req: Request, res: Response) => {
  try{
    const dto: BookCreateDto = req.body;

  
  if (!dto.name || typeof dto.name !== "string") {
      return res.status(400).send("Invalid or missing 'name'");
  }

  if (!Array.isArray(dto.authorIds) || dto.authorIds.some(id => typeof id !== "number")) {
      return res.status(400).send("Invalid or missing 'authorIds'");
  }

  if (!dto.year || typeof dto.year !== "number") {
      return res.status(400).send("Invalid or missing 'year'");
  }

  // Validacija autora
  const bookAuthors = dto.authorIds.map(id => {
      const author = authors.find(a => a.id === id);
      if (!author) {
          throw new Error(`Author with ID ${id} does not exist`);
      }
      return author;
  });

  const newBook: Book = {
      id: books.length + 1,
      name: dto.name,
      authors: bookAuthors,
      year: dto.year,
  };

  books.push(newBook);
  res.status(201).json(newBook);
  }catch (error: any) {
    // Obrada greške i vraćanje odgovora klijentu
    return res.status(400).json({ error: error.message });
  }
  
};

export const updateBook = (req: Request, res: Response) => {
  const id: number = Number(req.params.id); 
  if (isNaN(id)) {
      return res.status(400).send("Invalid ID format");
  }

  const dto: BookUpdateDto = req.body;

  if (dto.name !== undefined && typeof dto.name !== "string") {
      return res.status(400).send("Invalid 'name'");
  }

  if (dto.year !== undefined && typeof dto.year !== "number") {
      return res.status(400).send("Invalid 'year'");
  }

  if (dto.authorIds !== undefined && (!Array.isArray(dto.authorIds) || dto.authorIds.some(id => typeof id !== "number"))) {
      return res.status(400).send("Invalid 'authorIds'");
  }

  const book = books.find(b => b.id === id);
  if (!book) return res.status(404).send("Book not found");

  if (dto.name !== undefined) book.name = dto.name;
  if (dto.year !== undefined) book.year = dto.year;

  if (dto.authorIds) {
      const bookAuthors = dto.authorIds.map(id => {
          const author = authors.find(a => a.id === id);
          if (!author) {
              throw new Error(`Author with ID ${id} does not exist`);
          }
          return author;
      });
      book.authors = bookAuthors;
  }

  res.json(book);
};

export const deleteBook = (req: Request, res: Response) => {
    const id: number = Number(req.params.id); 
    if (isNaN(id)) {
        return res.status(400).send("Invalid ID format");
    }
    books = books.filter(b => b.id !== id);
    res.status(204).send();
};