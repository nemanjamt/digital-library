import { Router } from 'express';
import {
  getAllUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser,
} from '../controllers/userController';
import { validateUserId, validateUserData } from '../middlewares/userValidation';

const router = Router();

router.get('/', getAllUsers);
router.get('/:id', validateUserId, getUserById);
router.post('/', validateUserData, createUser);
router.put('/:id', validateUserId, validateUserData, updateUser);
router.delete('/:id', validateUserId, deleteUser);

export default router;
