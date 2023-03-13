package com.example.demo.security;

import org.springframework.context.annotation.Profile;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.authentication.preauth.PreAuthenticatedAuthenticationToken;
import org.springframework.security.web.authentication.preauth.PreAuthenticatedCredentialsNotFoundException;
import org.springframework.stereotype.Component;

@Component
@Profile({ "prod", "test" })
public class AutheliaAuthenticationManager implements AuthenticationManager {

  @Override
  public Authentication authenticate(Authentication authentication) throws AuthenticationException {
    if (authentication.getCredentials() == null) {
      throw new PreAuthenticatedCredentialsNotFoundException(
          "Authelia headers not found in request.");
    }

    AutheliaUser autheliaUser = (AutheliaUser) authentication.getPrincipal();

    return new PreAuthenticatedAuthenticationToken(
        authentication.getPrincipal(), authentication.getCredentials(),
        autheliaUser.getAuthorities());

  }

}
