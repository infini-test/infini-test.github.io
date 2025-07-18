package com.example.mp.code.service.impl;

import com.example.mp.code.entity.User;
import com.example.mp.code.mapper.UserMapper;
import com.example.mp.code.service.IUserService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.stereotype.Service;

/**
 * <p>
 * 用户表 服务实现类
 * </p>
 *
 * @author s4zuyf
 * @since 2025-06-15
 */
@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements IUserService {

}
