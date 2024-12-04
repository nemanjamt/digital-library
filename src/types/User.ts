export interface User {
    id: number;
    username: string;
    name: string;
    lastName: string;
    password: string;
}

export interface UserCreateDto {
    username: string;
    name: string,
    lastName: string;
    password: string
}

export interface UserDto {
    id: number;
    username: string;
    name: string;
    lastName: string;
}

export interface UserUpdateDto {
    username?: string;
    name?: string,
    lastName?: string;
}