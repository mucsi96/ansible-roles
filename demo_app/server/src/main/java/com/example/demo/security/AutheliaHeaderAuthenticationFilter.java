package com.example.demo.security;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.web.authentication.preauth.AbstractPreAuthenticatedProcessingFilter;

import jakarta.servlet.http.HttpServletRequest;

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

    if (username == null || groups == null || displayName == null || email == null) {
      return null;

    }

    return new AutheliaUser(username, groups, displayName, email);
  }

}

