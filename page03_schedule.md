---
layout: page
title: Schedule
description: 
img: BIO165_header.png 
caption: "BIO165 Quantitative Cell Biology - from molecules to evolution"
permalink: schedule
sidebar: true
---

# {{site.data.schedule.title}}
{{site.data.schedule.authors}}

{% for entry in site.data.about %}

{% if entry[0] != 'title' %}
{% if entry[0] != 'authors' %}
## {{entry[0]}}
{{entry[1]}}
{% endif %}
{% endif %}
{% endfor %}