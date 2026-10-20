from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


def _is_break(p):
    return "BREAK" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def _break_star(ctx):
    """100 damage to each of the opponent's Pokemon BREAK."""
    for p in list(ctx.opponent_pokemon_in_play()):
        if _is_break(p):
            await ctx.deal_damage(100, target=p, apply_modifiers=None)


card = PokemonCardDef(
    guid="5f919691-ad5d-5128-8541-83e036a17016",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StarmieBREAK.Name",
    display_name="Starmie BREAK",
    searchable_by=["Starmie BREAK", "BREAK", "StarmieBREAK"],
    subtypes=["BREAK"],
    collector_number=32,
    set_code="XY12",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Break Star",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon BREAK. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=_break_star,
        ),
    ],
)