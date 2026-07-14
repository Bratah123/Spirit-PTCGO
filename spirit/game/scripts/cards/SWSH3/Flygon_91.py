from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import (
    no_retreat_passive, is_in_active_spot, opposing_active, apply_protection,
)


async def desert_geyser(ctx):
    """If your opponent has a Stadium in play, discard it. If you discarded
    a Stadium in this way, during your opponent's next turn, prevent all
    damage from and effects of attacks done to this Pokemon."""
    await ctx.deal_damage()
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.opponent_id:
        discarded = await ctx.discard_stadium()
        if discarded is not None:
            await apply_protection(ctx, target=ctx.attacker, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="79e558c4-d9f2-5639-a2bb-bd4bc241d998",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=91,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Labyrinth of Sand",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon can't retreat.",
            passive=no_retreat_passive(
                lambda p, c: opposing_active(p, c) and is_in_active_spot(c)
            ),
        ),
        Attack(
            title="Desert Geyser",
            game_text="If your opponent has a Stadium in play, discard it. If you discarded a Stadium in this way, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=desert_geyser,
        ),
    ],
)