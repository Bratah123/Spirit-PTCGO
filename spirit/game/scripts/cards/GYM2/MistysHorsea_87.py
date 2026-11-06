from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import ink_spurt


card = PokemonCardDef(
    guid="078b1ec3-58f9-5c41-9cb2-4aa629971728",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysHorsea.Name",
    display_name="Misty's Horsea",
    searchable_by=["Misty's Horsea", "Basic", "MistysHorsea"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Ink Spurt",
            game_text="Flip a coin. If heads, whenever the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack does nothing. (This effect lasts until the Defending Pok\u00e9mon evolves or is Benched.)",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=ink_spurt,
        ),
    ],
)
