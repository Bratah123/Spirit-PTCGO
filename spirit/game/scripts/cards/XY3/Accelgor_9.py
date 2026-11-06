from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive


def _evolved_this_turn(ctx):
    """Accelgor only evolves from Shelmet: it entered play this turn."""
    ts = ctx.session.turn_state
    return ts.entered_play_turn.get(ctx.attacker.entity_id) == ts.turn_number


async def _afterimage_strike(ctx):
    """40; during the opponent's next turn, flip to prevent attack damage."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, flip_prevent_damage_passive("Afterimage Strike"))


card = PokemonCardDef(
    guid="49259a34-51ed-5a8b-b128-ec463f40b194",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor", "Stage 1", "Accelgor"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    abilities=[
        Attack(
            title="Raid",
            game_text="If this Pok\u00e9mon evolved from Shelmet during this turn, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_evolved_this_turn, 40),
        ),
        Attack(
            title="Afterimage Strike",
            game_text="If any damage is done to this Pok\u00e9mon by attacks during your opponent's next turn, flip a coin. If heads, prevent that damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_afterimage_strike,
        ),
    ],
)