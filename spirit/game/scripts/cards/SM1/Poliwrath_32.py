from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import AttrID


async def _wake_up_slap(ctx):
    """80, +80 if the opponent's Active has a Special Condition; then remove them all."""
    defender = ctx.defender
    affected = defender is not None and bool(defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
    await ctx.deal_damage(80 + (80 if affected else 0))
    if affected and defender.parent is not None:
        await ctx.cure_all_conditions(defender)


card = PokemonCardDef(
    guid="8bfc9ee7-38c4-526e-bd9f-5b316a5ee085",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Split Spiral Punch",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Wake-Up Slap",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 80 more damage. Then, remove all Special Conditions from that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=_wake_up_slap,
        ),
    ],
)