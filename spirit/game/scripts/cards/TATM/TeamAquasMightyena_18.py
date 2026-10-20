from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.content.definitions import def_for


async def _flip_discard_defender_energy(ctx):
    """Printed damage; flip a coin. If heads, discard an Energy attached to
    your opponent's Active Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard")


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


card = PokemonCardDef(
    guid="770ac1cf-fe03-5ce3-a92c-fe727fc8a6fa",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasMightyena.Name",
    display_name="Team Aqua's Mightyena",
    searchable_by=["Team Aqua's Mightyena", "Stage 1", "TeamAquasMightyena"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasPoochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Teampact",
            game_text="Flip a coin for each Team Aqua Pok\u00e9mon you have in play. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(per_heads=30, coins_from=lambda ctx: sum(1 for p in ctx.my_pokemon_in_play() if _team(p, "Aqua"))),
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_flip_discard_defender_energy,
        ),
    ],
)