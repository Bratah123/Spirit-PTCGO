from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


async def natures_judgment(ctx):
    """You may discard all Energy from this Pokémon. If you do, this attack
    does 80 more damage."""
    bonus = 0
    if ctx.attached_energies(ctx.attacker) and await ctx.ask_yes_no(
        "Discard all Energy from this Pokémon?"
    ):
        await ctx.discard_energy_from(ctx.attacker, 99)
        bonus = 80
    await ctx.deal_damage(80 + bonus)


card = PokemonCardDef(
    guid="26246f22-7dcd-5193-8746-d2170e058d70",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name",
    display_name="Tapu Bulu",
    searchable_by=["Tapu Bulu", "Basic", "TapuBulu"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=787,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Nature's Judgment",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=natures_judgment,
        ),
    ],
)