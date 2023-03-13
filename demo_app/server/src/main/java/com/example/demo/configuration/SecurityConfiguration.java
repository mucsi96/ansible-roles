package com.example.demo.configuration;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;

import com.example.demo.core.FilterChainExceptionHandler;
import com.example.demo.security.AutheliaHeaderAuthenticationFilter;

import lombok.RequiredArgsConstructor;

@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
@EnableMethodSecurity(jsr250Enabled = true)
public class SecurityConfiguration {

  @Bean
  SecurityFilterChain defaultSecurityFilterChain(
      HttpSecurity http,
      AutheliaHeaderAuthenticationFilter autheliaHeaderAuthenticationFilter,
      FilterChainExceptionHandler filterChainExceptionHandler)
      throws Exception {

    http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS);

    http.anonymous().disable();
    http.csrf().disable();
    http.headers().frameOptions().disable();
    http.formLogin().disable();
    http.logout().disable();

    http.addFilter(autheliaHeaderAuthenticationFilter);
    http.addFilterBefore(filterChainExceptionHandler, AutheliaHeaderAuthenticationFilter.class);

    return http.build();
  }
}
