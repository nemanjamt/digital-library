import { Request, Response, NextFunction } from 'express';

// Middleware to validate user ID
export const validateUserId = (req: Request, res: Response, next: NextFunction) => {
  const { id } = req.params;
  if (!Number.isInteger(Number(id))) {
    return res.status(400).json({ error: 'Invalid user ID' });
  }
  next();
};

// Middleware to validate user data
export const validateUserData = (req: Request, res: Response, next: NextFunction) => {
  const { username, email } = req.body;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!username || typeof username !== 'string' || !email || !emailRegex.test(email)) {
    return res.status(400).json({ error: 'Invalid user data' });
  }
  next();
};