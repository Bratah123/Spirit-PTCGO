from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import effective_max_hp


async def _damakinesis(ctx):
    """Move 6 damage counters from any of your Pokemon to the Defending Pokemon."""
    d = ctx.defender
    remaining = 6
    while d is not None and remaining > 0:
        pool = [p for p in ctx.my_pokemon_in_play()
                if p.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, p)]
        if not pool:
            break
        src = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(
            pool, f"Move damage counters from which Pokémon? ({remaining} left)")
        moved = await ctx.move_damage_counters(src or pool[0], d, max_count=remaining)
        if moved <= 0:
            break
        remaining -= moved


card = PokemonCardDef(
    guid="b901b866-2d57-54a0-8198-e651bab1bd51",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    display_name="Beheeyem",
    searchable_by=["Beheeyem", "Stage 1", "Team Plasma", "Beheeyem"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=70,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    family_id=605,
    abilities=[
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Damakinesis",
            game_text="Move 6 damage counters from any of your Pok\u00e9mon to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=_damakinesis,
        ),
    ],
)