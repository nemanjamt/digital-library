import express from 'express';
import bodyParser from 'body-parser';
import bookRoutes from './routes/bookRoutes';
import authorRoutes from './routes/authorRoutes';
import userRoutes from './routes/userRoutes';
import "reflect-metadata";

const app = express();
app.use(bodyParser.json());

app.use('/books', bookRoutes);
app.use('/authors', authorRoutes);
app.use('/users', userRoutes);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
