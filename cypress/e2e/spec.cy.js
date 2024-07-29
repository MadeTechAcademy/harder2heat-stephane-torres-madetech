const mockPropertyData = require("../../properties.json")
describe('template spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:5000')
  })
})

describe("The correct information for each property is displayed", () => {
  beforeEach(() => {
    cy.visit('http://localhost:5000')
  })
  it("has the correct number of properties displayed on the screen", () => {

    cy.get("p").contains(`${mockPropertyData.length}`)
  })

  it("had a list of property coordinates for each property", () => {
 mockPropertyData.forEach((building) => {
      cy.get("p").contains(`${building.geometry.coordinates[0]}`)
    })
  })
})