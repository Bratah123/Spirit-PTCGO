from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_supporter_card


async def _charge_dash(ctx):
    """70; you may do 20 more damage. If you do, this Pokemon does 20 to itself."""
    if await ctx.ask_yes_no("Do 20 more damage? If you do, this Pokémon does 20 damage to itself."):
        await ctx.deal_damage(90)
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(70)


card = PokemonCardDef(
    guid="8be74cba-f91a-57b2-a5d9-be9d45b43660",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name",
    display_name="Gogoat",
    searchable_by=["Gogoat", "Stage 1", "Gogoat"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    family_id=672,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for up to 2 Supporter cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_supporter_card, count=2, minimum=0, reveal=True,
                prompt='Choose up to 2 Supporter cards'),
        ),
        Attack(
            title="Charge Dash",
            game_text="You may do 20 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=_charge_dash,
        ),
    ],
)