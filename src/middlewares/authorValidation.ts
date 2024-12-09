import { Request, Response, NextFunction } from 'express';

// Middleware to validate author ID
export const validateAuthorId = (req: Request, res: Response, next: NextFunction) => {
  const { id } = req.params;
  if (!Number.isInteger(Number(id))) {
    return res.status(400).json({ error: 'Invalid author ID' });
  }
  next();
};

// Middleware to validate author data
export const validateAuthorData = (req: Request, res: Response, next: NextFunction) => {
  const { name, lastName } = req.body;
  if (!name || typeof name !== 'string' || !lastName || typeof lastName !== 'string') {
    return res.status(400).json({ error: 'Invalid author data' });
  }
  next();
};