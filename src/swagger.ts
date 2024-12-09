import swaggerJSDoc from 'swagger-jsdoc';
import swaggerUi from 'swagger-ui-express';
import { Express, Request, Response } from 'express';

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Digital Library API',
      version: '1.0.0',
      description: 'A project intended for the university course Cyber Security',
    },
    servers: [
      {
        url: 'http://localhost:3000',
      },
    ],
  },
  apis: ['./src/routes/*.ts', './src/controllers/*.ts'], // Paths to files containing OpenAPI definitions
};

const swaggerSpec = swaggerJSDoc(options);

export const setupSwagger = (app: Express) => {
  app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));
  // Route to serve the OpenAPI JSON specification
  app.get('/openapi.json', (req: Request, res: Response) => {
    res.setHeader('Content-Type', 'application/json');
    res.send(swaggerSpec);
  });
};