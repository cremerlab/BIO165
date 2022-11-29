---
layout: page
title: Coding
description: 
img: code.png 
caption: "BIO165 Quantitative Cell Biology - from molecules to evolution"
permalink: coding
sidebar: true
---

# {{site.data.coding.title}}
{{site.data.coding.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}