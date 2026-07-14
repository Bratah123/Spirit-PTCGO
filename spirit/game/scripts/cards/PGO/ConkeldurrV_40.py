from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def counter(ctx):
    """20 damage, +that much more if this Pokemon was damaged by an attack during the opponent's last turn."""
    bonus = ctx.damage_taken_last_turn(ctx.attacker)
    await ctx.deal_damage(20 + bonus)


card = PokemonCardDef(
    guid="a636cb92-fb8b-563d-a978-eb976e5123a6",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ConkeldurrV.Name",
    display_name="Conkeldurr V",
    searchable_by=["Conkeldurr V", "Basic", "V", "ConkeldurrV"],
    subtypes=["Basic", "V"],
    collector_number=40,
    set_code="PGO",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=534,
    abilities=[
        Attack(
            title="Counter",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=counter,
        ),
        Attack(
            title="Dynamic Punch",
            game_text="Flip a coin. If heads, this attack does 90 more damage, and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True, heads_bonus_damage=90),
        ),
    ],
)