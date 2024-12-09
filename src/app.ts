import express from 'express';
import bodyParser from 'body-parser';
import bookRoutes from './routes/bookRoutes';
import authorRoutes from './routes/authorRoutes';
import userRoutes from './routes/userRoutes';
import { setupSwagger } from './swagger';

const app = express();
app.use(bodyParser.json());

app.use('/books', bookRoutes);
app.use('/authors', authorRoutes);
app.use('/users', userRoutes);

setupSwagger(app);

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
  console.log(`Swagger docs available at http://localhost:${PORT}/api-docs`);
  console.log(`OpenAPI JSON available at http://localhost:${PORT}/openapi.json`);
});
