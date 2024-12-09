import { Router } from 'express';
import {
  getAllBooks,
  getBookById,
  createBook,
  updateBook,
  deleteBook,
} from '../controllers/bookController';
import { validateBookId, validateBookData } from '../middlewares/bookValidation';

const router = Router();

router.get('/', getAllBooks);
router.get('/:id', validateBookId, getBookById);
router.post('/', validateBookData, createBook);
router.put('/:id', validateBookId, validateBookData, updateBook);
router.delete('/:id', validateBookId, deleteBook);

export default router;
