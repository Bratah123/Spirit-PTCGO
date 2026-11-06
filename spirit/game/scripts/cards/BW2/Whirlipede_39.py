from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_bonus_attack


async def steamroller(ctx):
    """40 damage. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="413d29ab-fcaf-581a-8ffc-fe23f8c1b555",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    display_name="Whirlipede",
    searchable_by=["Whirlipede", "Stage 1", "Whirlipede"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Venoshock",
            game_text="If the Defending Pok\u00e9mon is Poisoned, this attack does 60 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=condition_bonus_attack(60, SpecialConditions.POISONED),
        ),
        Attack(
            title="Steamroller",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=steamroller,
        ),
    ],
)
