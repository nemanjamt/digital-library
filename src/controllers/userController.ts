import { Request, Response } from 'express';
import { User, UserDto } from '../types/User';
import { toUserDto, toUserDtoArray } from '../util/user.mapper';


const users: User[] = [];

export const getAllUsers = (req: Request, res: Response) => {
  res.json(toUserDtoArray(users)); 
};

export const getUserById = (req: Request, res: Response) => {
  const id: number = Number(req.params.id); 
  if (isNaN(id)) {
      return res.status(400).send("Invalid ID format");
  }
  const user = users.find((u) => u.id === id);
  if (!user) {
    res.status(404).send('User not found.');
    return;
  }
  res.json(toUserDto(user));
};

export const createUser = (req: Request, res: Response) => {
  const { id, username, name, lastName, password } = req.body as User;

  if (!id || !username || !name || !lastName || !password) {
    res.status(400).send('All fields are required.');
    return;
  }

  users.push({ id, username, name, lastName, password });
  res.status(201).send('User created successfully.');
};

export const updateUser = (req: Request, res: Response) => {
  const id: number = Number(req.params.id); // Konverzija u broj
  if (isNaN(id)) {
      return res.status(400).send("Invalid ID format");
  }
  const { username, name, lastName, password } = req.body;
  const user = users.find((u) => u.id === id);

  if (!user) {
    res.status(404).send('User not found.');
    return;
  }

  if (username) user.username = username;
  if (name) user.name = name;
  if (lastName) user.lastName = lastName;
  if (password) user.password = password;

  res.send('User updated successfully.');
};

export const deleteUser = (req: Request, res: Response) => {
  const id: number = Number(req.params.id); 
  if (isNaN(id)) {
      return res.status(400).send("Invalid ID format");
  }
  const index = users.findIndex((u) => u.id === id);
  if (index === -1) {
    res.status(404).send('User not found.');
    return;
  }
  users.splice(index, 1);
  res.send('User deleted successfully.');
};
