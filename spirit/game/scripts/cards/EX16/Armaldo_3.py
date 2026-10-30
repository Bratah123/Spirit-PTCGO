"""STUB: effect not implemented — do not guess mechanics.
Armaldo (EX16 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import rock_blast_discard_fighting
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def puncture(ctx):
    """This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="49bd496d-9d35-5b71-b1d8-b473c3798e61",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name",
    display_name="Armaldo",
    searchable_by=["Armaldo", "Stage 2", "Armaldo"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    family_id=347,
    abilities=[
        Attack(
            title="Rock Blast",
            game_text="Discard up to 5 Fighting Energy cards attached to Armaldo. For each Energy card you discarded, choose an opponent's Pok\u00e9mon in play and this attack does 20 damage to those Pok\u00e9mon. (You may choose the same Pok\u00e9mon more than once.) This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=rock_blast_discard_fighting(5, 20),
        ),
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=puncture,
        ),
    ],
)