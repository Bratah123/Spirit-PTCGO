from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks, recoil_attack
from spirit.game.session.effects import is_basic_pokemon


async def freeze_down(ctx):
    """40. If the Defending Pokemon is a Basic Pokemon, it can't attack
    during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_basic_pokemon(defender):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="ae268100-fbfc-59a1-b494-8cec412af018",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glastrier.Name",
    display_name="Glastrier",
    searchable_by=["Glastrier", "Basic", "Glastrier"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=896,
    abilities=[
        Attack(
            title="Freeze Down",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=freeze_down,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=recoil_attack(30),
        ),
    ],
)