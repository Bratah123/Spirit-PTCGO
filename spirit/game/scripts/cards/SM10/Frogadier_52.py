from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive

async def _afterimage_strike(ctx):
    """40; during the opponent's next turn, flip to prevent attack damage."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(
        ctx.attacker, flip_prevent_damage_passive("Afterimage Strike"))

card = PokemonCardDef(
    guid="24dc1611-8aca-5c33-a2fc-9334540f46e3",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    display_name="Frogadier",
    searchable_by=["Frogadier", "Stage 1", "Frogadier"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Afterimage Strike",
            game_text="If any damage is done to this Pok\u00e9mon by attacks during your opponent's next turn, flip a coin. If heads, prevent that damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_afterimage_strike,
        ),
    ],
)