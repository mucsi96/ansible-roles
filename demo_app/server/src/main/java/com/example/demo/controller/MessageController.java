package com.example.demo.controller;

import com.example.demo.config.MessageConfig;
import com.example.demo.repository.MessageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class MessageController {
    private final MessageRepository messageRepository;

    @GetMapping("/message")
    public String getMessage() {
        return messageRepository.findAll().get(0).getContent();
    }
}
