import { User, UserDto } from "../types/User";

export const toUserDto = (user: User): UserDto => {
  const { id, username, name, lastName } = user;
  return { id, username, name, lastName };
};

export const toUserDtoArray = (users: User[]): UserDto[] => {
  return users.map(toUserDto);
};
