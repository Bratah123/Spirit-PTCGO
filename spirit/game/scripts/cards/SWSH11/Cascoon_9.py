from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when


async def harden(ctx):
    """During the opponent's next turn, prevent all attack damage to this
    Pokemon that is 60 or less."""
    ctx.add_passive_through_opponents_turn(
        ctx.source, prevent_damage_when(lambda calc, c: calc.amount <= 60)
    )


card = PokemonCardDef(
    guid="0ea9c8a0-5b43-55db-b364-706d453c128e",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    display_name="Cascoon",
    searchable_by=["Cascoon", "Stage 1", "Cascoon"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks if that damage is 60 or less.",
            cost={PokemonTypes.GRASS: 1},
            effect=harden,
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)