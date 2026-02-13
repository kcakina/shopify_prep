## API Endpoints

### POST /exchanges
Create a new Secret Santa exchange.  
Returns the exchange ID used for all subsequent operations.

### POST /exchanges/{id}/participants
Add a participant to an existing exchange.

### POST /exchanges/{id}/exclusions
Add an exclusion rule preventing a specific participant from being assigned to another participant.

### POST /exchanges/{id}/generate
Generate Secret Santa assignments for the exchange using the current participants and exclusions.  
Returns an error if no valid assignment is possible.

### GET /exchanges/{id}/reveal?token=...
Reveal the assigned recipient for a single participant using a secure reveal token.  
Only returns that participant’s assignment.
