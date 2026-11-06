from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import energy_kick


card = PokemonCardDef(
    guid="bda34a9e-e50d-5194-abd9-7dd6b864794d",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid",
    searchable_by=["Elekid", "Baby", "Elekid"],
    subtypes=["Baby"],
    collector_number=9,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=239,
    abilities=[
        Attack(
            title="Energy Kick",
            game_text="Flip a coin. If heads, choose an Energy card attached to the Defending Pok\u00e9mon. Your opponent moves that card to 1 of his or her other Pok\u00e9mon. (If your opponent has no Benched Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=energy_kick,
        ),
    ],
)
