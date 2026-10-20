from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_basic_pokemon


async def _tail_swing(ctx):
    """100; 20 damage to each of the opponent's Benched Basic Pokemon."""
    await ctx.deal_damage()
    for p in list(ctx.opponent_bench()):
        if is_basic_pokemon(p):
            await ctx.deal_damage(20, target=p, apply_modifiers=None)


card = PokemonCardDef(
    guid="869166ec-76fe-5519-8a19-30128c4e9988",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Rumble",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Tail Swing",
            game_text="This attack does 20 damage to each of your opponent's Benched Basic Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=_tail_swing,
        ),
    ],
)