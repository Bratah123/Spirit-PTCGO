"""STUB: effect not implemented — do not guess mechanics.
Gothitelle (XY3 #41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _scout(ctx):
    """Your opponent reveals their hand."""
    await ctx.reveal_hand(ctx.opponent_id)


card = PokemonCardDef(
    guid="9eb1697f-42bb-58a6-9a40-68fe2daa79ff",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Ability(
            title="Teleport Room",
            game_text="Once during your turn (before your attack), you may discard any Stadium card in play. If you do, put a Stadium card with a different name from your discard pile into play.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Psy Report",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=_scout,
        ),
    ],
)