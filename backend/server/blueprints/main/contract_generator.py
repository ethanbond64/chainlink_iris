


class ContractWriter:

    def __init__(self,name,event_id,env):
        # Contract name for reference
        self.name = name
        # Event Id to fill into api
        self.event_id = event_id
        # JSON blob that contains sensitive data
        # TODO learn how to handle sensitive data in smart contract
        self.env = env

    # Tie it all together
    def write(self):
        return
    
    # save the file as a real sol file in a gen file 
    def fill_template(self):
        return

    # Optional getter to view the text
    def get_contract_text():
        return