<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/livres">
    <livres>
      <xsl:for-each select="livre">
        <livre>
          <xsl:attribute name="annee">
            <xsl:value-of select="annee_parution"/>
          </xsl:attribute>
          <xsl:attribute name="genre">
            <xsl:value-of select="genre"/>
          </xsl:attribute>
          <xsl:value-of select="concat(titre, ' - ', auteur)"/>
        </livre>
      </xsl:for-each>
    </livres>
  </xsl:template>
</xsl:stylesheet>
