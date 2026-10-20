from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive
from spirit.game.card_effects.attacks_common import bonus_if, named_in_play


async def _cavalry_lance(ctx):
    """Printed damage; during your opponent's next turn this Pokémon has no Weakness."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, no_weakness_passive())


card = PokemonCardDef(
    guid="b6757a74-b697-5942-97b3-2a8332d6e9b8",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title="Aurora Gain",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no weakness.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_cavalry_lance,
        ),
        Attack(
            title="Light of Life",
            game_text="If your opponent has Yveltal (including Yveltal-EX) in play, this attack does 40 more damage.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(named_in_play('Yveltal', 'Yveltal-EX', side='opponent'), 40),
        ),
    ],
)