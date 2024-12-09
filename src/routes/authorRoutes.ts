import { Router } from 'express';
import {
  getAllAuthors,
  getAuthorById,
  createAuthor,
  updateAuthor,
  deleteAuthor,
} from '../controllers/authorController';
import { validateAuthorId, validateAuthorData } from '../middlewares/authorValidation';

const router = Router();

/**
 * @swagger
 * /authors:
 *   get:
 *     summary: Get all authors
 *     responses:
 *       200:
 *         description: List of authors
 */
router.get('/', getAllAuthors);

/**
 * @swagger
 * /authors/{id}:
 *   get:
 *     summary: Get author by ID
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Author details
 *       404:
 *         description: Author not found
 */
router.get('/:id', validateAuthorId, getAuthorById);

/**
 * @swagger
 * /authors:
 *   post:
 *     summary: Create a new author
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               name:
 *                 type: string
 *               lastName:
 *                 type: string
 *     responses:
 *       201:
 *         description: Author created successfully
 */
router.post('/', validateAuthorData, createAuthor);

/**
 * @swagger
 * /authors/{id}:
 *   put:
 *     summary: Update an author
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               name:
 *                 type: string
 *               lastName:
 *                 type: string
 *     responses:
 *       200:
 *         description: Author updated successfully
 *       404:
 *         description: Author not found
 */
router.put('/:id', validateAuthorId, validateAuthorData, updateAuthor);

/**
 * @swagger
 * /authors/{id}:
 *   delete:
 *     summary: Delete an author
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Author deleted successfully
 *       404:
 *         description: Author not found
 */
router.delete('/:id', validateAuthorId, deleteAuthor);

export default router;
