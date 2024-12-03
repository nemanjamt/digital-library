import { Request, Response } from 'express';
import { Book } from '../types/Book';


const books: Book[] = []; 

export const getAllBooks = (req: Request, res: Response): void => {
  res.json(books);
};

export const getBookById = (req: Request, res: Response): void => {
  const book = books.find((b) => b.id === req.params.id);
  if (!book) {
    res.status(404).send('Book not found.');
    return;
  }
  res.json(book);
};


export const createBook = (req: Request, res: Response): void => {
  const { id, name, authors, year } = req.body as Book;

  if (!id || !name || !authors || !year) {
    res.status(400).send('All fields are required.');
    return;
  }

  for (const author of authors) {
    if (!author.id || !author.name || !author.lastName) {
      res.status(400).send('Each author must have id, name, and lastName.');
      return;
    }
  }

  books.push({ id, name, authors, year });
  res.status(201).send('Book created successfully.');
};

export const updateBook = (req: Request, res: Response): void => {
  const { name, authors, year } = req.body;
  const book = books.find((b) => b.id === req.params.id);

  if (!book) {
    res.status(404).send('Book not found.');
    return;
  }

  if (name) book.name = name;
  if (authors) book.authors = authors;
  if (year) book.year = year;

  res.send('Book updated successfully.');
};

export const deleteBook = (req: Request, res: Response): void => {
  const index = books.findIndex((b) => b.id === req.params.id);
  if (index === -1) {
    res.status(404).send('Book not found.');
    return;
  }
  books.splice(index, 1);
  res.send('Book deleted successfully.');
};
