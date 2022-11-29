---
layout: page
title: Prerequisites
description: 
img: BIO165_header.png 
%caption: "BIO165 Quantitative Cell Biology - from molecules to evolution"
permalink: prerequisite
sidebar: true
---

# {{site.data.prerequisite.title}}
{{site.data.prerequisite.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}