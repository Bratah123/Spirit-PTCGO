from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack


async def cosmicsplosion(ctx):
    """190 damage, then this Pokémon is Knocked Out."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        await ctx.knock_out(ctx.attacker)


card = PokemonCardDef(
    guid="70be3724-5c22-57f9-81ee-932975cd9864",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name",
    display_name="Minior",
    searchable_by=["Minior", "Basic", "Minior"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=774,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Cosmicsplosion",
            game_text="This Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=190,
            effect=cosmicsplosion,
        ),
    ],
)
