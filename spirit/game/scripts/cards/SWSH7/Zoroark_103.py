from spirit.game.card_effects.pokemon import (
    phantom_transformation, phantom_transformation_condition,
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70524621-a475-5f65-a10d-2d26bd45b236",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1", "Zoroark"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Ability(
            title="Phantom Transformation",
            game_text="Once during your turn, you may choose a Stage 1 Pok\u00e9mon, except any Zoroark, from your discard pile. If you do, discard this Pok\u00e9mon and all attached cards, and put the chosen Pok\u00e9mon in its place.",
            activation=Activations.ONCE_PER_TURN,
            condition=phantom_transformation_condition,
            effect=phantom_transformation,
        ),
        Attack(
            title="Night Daze",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)