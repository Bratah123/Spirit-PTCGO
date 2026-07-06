from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf23d7f0-f5cf-5233-ad80-8aba42de925e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformRainyForm.Name",
    display_name="Castform Rainy Form",
    searchable_by=["Castform Rainy Form", "Basic", "CastformRainyForm"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pok\u00e9mon's attack costs.",
            effect=unimplemented,
        ),
        Attack(
            title="Rainfall",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)