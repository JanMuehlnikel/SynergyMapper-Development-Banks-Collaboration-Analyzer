"""
CONSTANTS.py defines variables that are needed throughout this application
"""

# ORGANISATIONS defines a dict with all Organizations in this Project with its abbreviation and  IATI Code

ORGANIZATIONS = {
    "BMZ": ["Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung", "bmz", "DE-1"],
    "IAD": ["Inter-American Development Bank", "iad", "XI-IATI-IADB"],
    "ADB": ["Asian Development Bank", "adb", "XM-DAC-46004"],
    "AfDB": ["African Development Bank", "afdb", "XM-DAC-46002"],
    "EIB": ["European Investment Bank", "eib", "XM-DAC-918-3"],
    "WB": ["The World Bank", "wb", "44000"],
    "WBTF": ["World Bank Trust Funds", "wbtf", "XI-IATI-WBTF"],
    "GIZ-NON-BMZ": ["Non BMZ GIZ Activity", "giz-non-bmz", "XM-DAC-5-52"],
    "AA": ["Auswärtiges Amt", "aa", "XM-DAC-5-7"]
}

SECONDARY_ORGANIZATIONS = {
    "giz": ["GIZ", "Deutsche Gesellschaft für Internationale Zusammenarbeit GmbH", "XM-DAC-5-52"],
    "kfw": ["KfW", "Kreditanstalt für Wiederaufbau", "XM-DAC-5-2"],
    "aa-other": ["AA", "Auswärtiges Amt (other client)"]
}

ORGA_SEARCH = {
    "BMZ": ["Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung"],
    "IAD": ["Inter-American Development Bank"],
    "ADB": ["Asian Development Bank", "adb"],
    "AfDB": ["African Development Bank"],
    "EIB": ["European Investment Bank"],
    "WB": ["The World Bank"],
    "WBTF": ["World Bank Trust Funds"],
    "AA-OTHER": ["Auswärtiges Amt - Other Customer"],
    "GIZ": ["Deutsche Gesellschaft für Internationale Zusammenarbeit GmbH"],
    "KFW": ["Kreditanstalt für Wiederaufbau"],
}

# IATI_ATTRIBUTES contains all relevant IATI Attributes that have to be fetched

IATI_ATTRIBUTES = [
    "iati_identifier",
    "title_narrative",
    "title_narrative_xml_lang",
    "reporting_org_ref",
    "participating_org_ref",
    "description_narrative_xml_lang",
    "description_narrative",
    "recipient_country_code",
    "recipient_region_code",
    "activity_status_code",
    "last_updated_datetime",
    "sector_code",
    "sector_vocabulary",
]