<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns="http://www.w3.org/TR/xhtml1/strict"
  xmlns:tei="http://www.tei-c.org/ns/1.0">
  <xsl:template match="/">
    <xsl:apply-templates/>
  </xsl:template>
  <xsl:template match="tei:teiHeader"/>
  <xsl:template match="tei:lb">
    <xsl:text> </xsl:text>
  </xsl:template>
</xsl:stylesheet>