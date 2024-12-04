export interface Author {
    id: number;
    name: string;
    lastName: string;
}

export interface AuthorCreateDto{
  name?:string;
  lastName?:string;
}

export interface AuthorUpdateDto{
  name?:string;
  lastName?:string;
}