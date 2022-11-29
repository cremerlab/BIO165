---
layout: page
title: Projects
description: 
img: BIO165_header.png 
caption: "BIO165 Quantitative Cell Biology - from molecules to evolution"
permalink: projects
sidebar: true
---

# {{site.data.projects.title}}
{{site.data.projects.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}