from enum import Enum, auto


class ResponseParser:
    '''
    Parse specific responses.\n
    
    This class' primary use is to parse very specific api call responses.\n
    Created to avoid cluttering methods with ugly dictionary searching (all api call responses return JSON)
    '''
    
    @staticmethod
    def parse_membership_details(response):
        return [response['Response']['destinyMemberships'][0]['membershipType'],
                response['Response']['destinyMemberships'][0]['membershipId']]
        
    @staticmethod
    def parse_character_details(response):
        return response['Response']['characters']['data'] # NOT DONE
    