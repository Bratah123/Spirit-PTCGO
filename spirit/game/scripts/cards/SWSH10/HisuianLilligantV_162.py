from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="f56c45f0-5bbe-58e5-9b53-05ca31c117b5",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligantV.Name",
    display_name="Hisuian Lilligant V",
    searchable_by=["Hisuian Lilligant V", "Basic", "V", "HisuianLilligantV"],
    subtypes=["Basic", "V"],
    collector_number=162,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=549,
    abilities=[
        Attack(
            title="Dance Gracefully",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={},
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)