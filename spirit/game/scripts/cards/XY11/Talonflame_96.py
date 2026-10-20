"""STUB: effect not implemented — do not guess mechanics.
Talonflame (XY11 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _aero_blitz(ctx):
    """40; search your deck for up to 2 cards and put them into your hand; shuffle."""
    await ctx.deal_damage()
    picked = await ctx.search_deck(None, 2, minimum=0, prompt="Choose up to 2 cards")
    if picked:
        await ctx.put_in_hand(picked, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="d7899595-c1ec-54f6-b766-37fe395384b2",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Ability(
            title="Gale Wings",
            game_text="If this Pok\u00e9mon is in your hand when you are setting up to play, you may put it face down as your Active Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aero Blitz",
            game_text="Search your deck for up to 2 cards and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=_aero_blitz,
        ),
    ],
)