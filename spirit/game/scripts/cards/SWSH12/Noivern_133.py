from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="15764b2e-e508-5267-a4f9-8e201d92b1c3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    display_name="Noivern",
    searchable_by=["Noivern", "Stage 1", "Noivern"],
    subtypes=["Stage 1"],
    collector_number=133,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Radiant Hunt",
            game_text="Knock Out 1 of your opponent's Radiant Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Seventh Echo",
            game_text="Draw cards until you have 7 cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)