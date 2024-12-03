import { Request, Response } from 'express';
import { Author } from '../types/Author';


const authors: Author[] = []; 

export const getAllAuthors = (req: Request, res: Response): void => {
  res.json(authors);
};

export const getAuthorById = (req: Request, res: Response): void => {
  const author = authors.find((a) => a.id === req.params.id);
  if (!author) {
    res.status(404).send('Author not found.');
    return;
  }
  res.json(author);
};

export const createAuthor = (req: Request, res: Response): void => {
  const { id, name, lastName } = req.body as Author;

  if (!id || !name || !lastName) {
    res.status(400).send('All fields are required.');
    return;
  }

  authors.push({ id, name, lastName });
  res.status(201).send('Author created successfully.');
};

export const updateAuthor = (req: Request, res: Response): void => {
  const { name, lastName } = req.body;
  const author = authors.find((a) => a.id === req.params.id);

  if (!author) {
    res.status(404).send('Author not found.');
    return;
  }

  if (name) author.name = name;
  if (lastName) author.lastName = lastName;

  res.send('Author updated successfully.');
};

export const deleteAuthor = (req: Request, res: Response): void => {
  const index = authors.findIndex((a) => a.id === req.params.id);
  if (index === -1) {
    res.status(404).send('Author not found.');
    return;
  }
  authors.splice(index, 1);
  res.send('Author deleted successfully.');
};
