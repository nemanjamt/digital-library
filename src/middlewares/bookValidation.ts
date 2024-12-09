import { Request, Response, NextFunction } from 'express';

// Middleware to validate book ID
export const validateBookId = (req: Request, res: Response, next: NextFunction) => {
  const { id } = req.params;
  if (!Number.isInteger(Number(id))) {
    return res.status(400).json({ error: 'Invalid book ID' });
  }
  next();
};

// Middleware to validate book data
export const validateBookData = (req: Request, res: Response, next: NextFunction) => {
  const { title, authorId } = req.body;
  if (!title || typeof title !== 'string' || !Number.isInteger(Number(authorId))) {
    return res.status(400).json({ error: 'Invalid book data' });
  }
  next();
};