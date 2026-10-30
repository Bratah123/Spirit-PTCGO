from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import amnesia


card = PokemonCardDef(
    guid="d0d6d1d3-723c-50b4-b4c7-fc1ea71e60c9",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    display_name="Lileep",
    searchable_by=["Lileep", "Stage 1", "Lileep"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RootFossil.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=amnesia,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
