%global gem_name fluent-plugin-grok-parser

Name: td-agent-%{gem_name}
Version: 2.5.1
Release: 3%{?dist}
Summary: Fluentd plugin to support Logstash-inspired Grok format for parsing logs
License: Apache-2.0
URL: https://github.com/fluent/fluent-plugin-grok-parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: td-agent3
BuildArch: noarch

%description
Fluentd plugin to support Logstash-inspired Grok format for parsing logs.

%install
%{__install} -m 0755 -d %{buildroot}/tmp
%{__install} -m 0644 %{SOURCE0} %{buildroot}/tmp/%{gem_name}-%{version}.gem

%post
td-agent-gem install --local /tmp/%{gem_name}-%{version}.gem

%files
/tmp/%{gem_name}-%{version}.gem
