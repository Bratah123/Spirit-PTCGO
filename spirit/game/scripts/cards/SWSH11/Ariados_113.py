from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def string_bind(ctx):
    """10, plus 30 for each [C] in the opponent's Active's Retreat Cost."""
    active = ctx.opponent_active()
    retreat = int(active.get_attribute(AttrID.RETREAT_COST) or 0) if active else 0
    await ctx.deal_damage(10 + 30 * retreat)


card = PokemonCardDef(
    guid="fe72c2d9-d868-5e86-8182-ba9e0b792544",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="String Bind",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=string_bind,
        ),
        Attack(
            title="Venomous Fang",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
