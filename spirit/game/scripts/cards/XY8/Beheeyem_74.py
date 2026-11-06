from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _mind_bullet(ctx):
    """20 to 1 of your opponent's Pokemon times the Energy attached to it."""
    opp = ctx.opponent_pokemon_in_play()
    if not opp:
        return
    target = opp[0] if len(opp) == 1 else await ctx.choose_pokemon(opp, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        n = len(ctx.attached_energies(target))
        if n:
            await ctx.deal_damage(20 * n, target=target)


card = PokemonCardDef(
    guid="79c69323-1630-550c-b0e1-147551a0eb1c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    display_name="Beheeyem",
    searchable_by=["Beheeyem", "Stage 1", "Beheeyem"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    family_id=605,
    abilities=[
        Attack(
            title="Mind Bullet",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon times the amount of Energy attached to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_mind_bullet,
        ),
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)