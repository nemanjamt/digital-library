import { Request, Response } from 'express';
import { Author } from '../types/Author';


export const authors: Author[] = []; 

export const getAllAuthors = (req: Request, res: Response): void => {
  res.json(authors);
};

export const getAuthorById = (req: Request, res: Response): void => {
  const id = Number(req.params.id); 

  if (isNaN(id)) {
    res.status(400).send('Invalid ID format. ID must be a number.');
    return;
  }

  const author = authors.find((a) => a.id === id);
  if (!author) {
    res.status(404).send('Author not found.');
    return;
  }
  res.json(author);
};

export const createAuthor = (req: Request, res: Response): void => {
  const { name, lastName } = req.body as Author;
  const id = authors.length + 1;
  if (!id || !name || !lastName) {
    res.status(400).send('All fields are required.');
    return;
  }

  authors.push({ id, name, lastName });
  res.status(201).send('Author created successfully.');
};

export const updateAuthor = (req: Request, res: Response): void => {
  const { name, lastName } = req.body;
  const id = Number(req.params.id); 

  if (isNaN(id)) {
    res.status(400).send('Invalid ID format. ID must be a number.');
    return;
  }
  const author = authors.find((a) => a.id === id);

  if (!author) {
    res.status(404).send('Author not found.');
    return;
  }

  if (name) author.name = name;
  if (lastName) author.lastName = lastName;

  res.send('Author updated successfully.');
};

export const deleteAuthor = (req: Request, res: Response): void => {
  const id = Number(req.params.id);

  if (isNaN(id)) {
    res.status(400).send('Invalid ID format. ID must be a number.');
    return;
  }

  const index = authors.findIndex((a) => a.id === id);
  if (index === -1) {
    res.status(404).send('Author not found.');
    return;
  }
  authors.splice(index, 1);
  res.send('Author deleted successfully.');
};
