Feature: Differing connectivities
  Depending on the connectivity of a building
  As a user I would like it displayed differently

Scenario: Building has old connectivity reads new connectivity
  When a building has <old_connectivity>
  Then it should read <new_connectivity>

        | old_connectivity | new_connectivity |

        | Standalone       | Free-Standing    |
        | Semi-Connected   | Dual-Connected   |
        | End Connected    | Single Connected |
