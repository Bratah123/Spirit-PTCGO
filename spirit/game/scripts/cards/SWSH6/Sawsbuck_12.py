from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

_stadium_in_play = lambda ctx: ctx.stadium_in_play() is not None

card = PokemonCardDef(
    guid="d22ab419-aaf3-5044-9fbc-947250e38997",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name",
    display_name="Sawsbuck",
    searchable_by=["Sawsbuck", "Stage 1", "Sawsbuck"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name",
    family_id=585,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Winter Horn",
            game_text="If you have a Stadium in play, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_stadium_in_play, 80),
        ),
    ],
)