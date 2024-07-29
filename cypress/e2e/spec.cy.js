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

  it("has a list of property coordinates for each property", () => {

      cy.get("ul").each(($ul, buildingNo) => {
          cy.wrap($ul).within(($ul) => {
              cy.get("li").each(($li,index) => {
                  cy.wrap($li).should("contain.text", `${mockPropertyData[buildingNo].geometry.coordinates[0][index]}`)
              })
          })

      })

    })

 })

// .each(($li, index) => {
//                 cy.wrap($li[1]).should('contain.text',)
//                 })