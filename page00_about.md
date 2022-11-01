---
layout: page
title: About
description: 
img: corona_virus_goodsell.jpg 
caption: "Courtesy of David S. Goodsell"
permalink: index.html
sidebar: true
---

# {{site.data.about.title}}
{{site.data.about.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}