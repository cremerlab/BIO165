---
layout: page
title: Description
description: 
img: BIO165_header.png 
caption: "BIO165 Quantitative Cell Biology - from molecules to evolution"
permalink: description
sidebar: true
---

# {{site.data.description.title}}
{{site.data.description.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}