import sqlite3
import json

from enum import Enum
from ..api_client import BungieAccount, ApiEndpointCaller


class EndpointComponentTypes(Enum):
    PROFILES = 100
    VENDORRECEIPTS = 101
    PROFILEINVENTORIES = 102
    PROFILECURRENCIES = 103
    CHARACTERS = 200
    CHARACTERINVENTORIES = 201
    CHARACTERPROGRESSIONS = 202
    CHARACTERRENDERDATA = 203
    CHARACTERACTIVITIES = 204
    CHARACTEREQUIPMENT = 205
    ITEMINSTANCES = 300
    ITEMOBJECTIVES = 301
    ITEMPERKS = 302
    ITEMRENDERDATA = 303
    ITEMSTATS = 304
    ITEMSOCKETS = 305
    ITEMTALENTGRIDS = 306
    ITEMCOMMONDATA = 307
    ITEMPLUGSTATES = 308
    VENDORS = 400
    VENDORCATEGORIES = 401
    VENDORSALES = 402
    KIOSKS = 500

# Connection to manifest containing sqlite3 file.
conn = sqlite3.connect('current_destiny_manifest.sqlite3')


class DestinyPlaceDefinition:
    pass

class DestinyActivityDefinition:
    pass

class DestinyActivityTypeDefinition:
    pass

class DestinyClassDefinition:
    pass

class DestinyGenderDefinition:
    pass

class DestinyInventoryBucketDefinition:
    pass

class DestinyRaceDefinition:
    pass

class DestinyTalentGridDefinition:
    pass

class DestinyUnlockDefinition:
    pass

class DestinySandboxPerkDefinition:
    pass

class DestinyStatGroupDefinition:
    pass

class DestinyFactionDefinition:
    pass

class DestinyVendorGroupDefinition:
    pass

class DestinyRewardSourceDefinition:
    pass

class DestinyItemCategoryDefinition:
    pass

class DestinyDamageTypeDefinition:
    pass

class DestinyActivityModeDefinition:
    pass

class DestinyMedalTierDefinition:
    pass

class DestinyAchievementDefinition:
    pass

class DestinyActivityGraphDefinition:
    pass

class DestinyBondDefinition:
    pass

class DestinyCollectibleDefinition:
    pass

class DestinyDestinationDefinition:
    pass

class DestinyEquipmentSlotDefinition:
    pass

class DestinyEventCardDefinition:
    pass

class DestinyStatDefinition:
    pass

class DestinyInventoryItemDefinition:
    pass

class DestinyItemTierTypeDefinition:
    pass

class DestinyLocationDefinition:
    pass

class DestinyLoreDefinition:
    pass

class DestinyMaterialRequirementSetDefinition:
    pass

class DestinyMetricDefinition:
    pass

class DestinyObjectiveDefinition:
    pass

class DestinyPlugSetDefinition:
    pass

class DestinyPowerCapDefinition:
    pass

class DestinyPresentationNodeDefinition:
    pass

class DestinyProgressionDefinition:
    pass

class DestinyProgressionLevelRequirementDefinition:
    pass

class DestinyRecordDefinition:
    pass

class DestinySackRewardItemListDefinition:
    pass

class DestinySandboxPatternDefinition:
    pass

class DestinySeasonDefinition:
    pass

class DestinySeasonPassDefinition:
    pass

class DestinySocketCategoryDefinition:
    pass

class DestinySocketTypeDefinition:
    pass

class DestinyTraitDefinition:
    pass

class DestinyTraitCategoryDefinition:
    pass

class DestinyVendorDefinition:
    
    @staticmethod
    def get_vendor(account: BungieAccount):
        
        cursor = conn.execute('SELECT id, json FROM DestinyVendorDefinition WHERE id > 0')
        response = [json.loads(row[1]) for row in cursor]

        for object in response:
            if object['displayProperties']['name'] == 'Ada-1':
                vendor_hash = object['hash'], object['displayProperties']['name']

        conn.close()
        
        return f'/Destiny2/{account.membership_details["membershipType"]}/Profile/{account.membership_details["destinyMembershipId"]}/Character/{account.characeters["Hunter"]}/Vendors/{vendor_hash}/'
        
        
    @staticmethod
    def get_vendors():
        pass

class DestinyMilestoneDefinition:
    pass

class DestinyActivityModifierDefinition:
    pass

class DestinyReportReasonCategoryDefinition:
    pass

class DestinyArtifactDefinition:
    pass

class DestinyBreakerTypeDefinition:
    pass

class DestinyChecklistDefinition:
    pass

class DestinyEnergyTypeDefinition:
    pass

class DestinyHistoricalStatsDefinition:
    pass