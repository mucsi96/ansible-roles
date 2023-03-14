package com.example.demo.security;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.web.authentication.preauth.AbstractPreAuthenticatedProcessingFilter;

import jakarta.servlet.http.HttpServletRequest;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class AutheliaHeaderAuthenticationFilter extends AbstractPreAuthenticatedProcessingFilter {

  public AutheliaHeaderAuthenticationFilter(AuthenticationManager authenticationManager) {
    this.setAuthenticationManager(authenticationManager);
    this.setContinueFilterChainOnUnsuccessfulAuthentication(false);
  }

  @Override
  protected Object getPreAuthenticatedPrincipal(HttpServletRequest request) {
    AutheliaUser user = getAutheliaUser(request);

    if (user == null) {
      return "N/A";
    }

    return user;
  }

  @Override
  protected Object getPreAuthenticatedCredentials(HttpServletRequest request) {
    return getAutheliaUser(request);
  }

  private AutheliaUser getAutheliaUser(HttpServletRequest request) {
    String username = request.getHeader("Remote-User");
    String groups = request.getHeader("Remote-Group");
    String displayName = request.getHeader("Remote-Name");
    String email = request.getHeader("Remote-Email");

    log.info("Authenticating using AutheliaHeaderAuthenticationFilter");
    log.info("username: %s, groups: %s, displayName: %s, email: %s", username, groups, displayName, email);

    if (username == null || groups == null || displayName == null || email == null) {
      log.info("Insuficient header data for authentication.");
      return null;
    }

    log.info("Creating AutheliaUser...");

    return new AutheliaUser(username, groups, displayName, email);
  }

}

