from spirit.game.card_effects.ex import explosive_evolution
"""STUB: effect not implemented — do not guess mechanics.
Dark Pupitar (EX7 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def double_wing_attack(ctx):
    """Does 20 damage to each Defending Pokémon (no printed damage)."""
    await ctx.deal_damage(20)


card = PokemonCardDef(
    guid="b8968894-ec26-5b89-8e31-f322b7351aae",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPupitar.Name",
    display_name="Dark Pupitar",
    searchable_by=["Dark Pupitar", "Stage 1", "DarkPupitar"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Explosive Evolution",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance.) Then, search your deck for a card that evolves from Dark Pupitar and put it on Dark Pupitar. (This counts as evolving Dark Pupitar.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=explosive_evolution(),
        ),
        Attack(
            title="Double Tackle",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=double_wing_attack,
        ),
    ],
)