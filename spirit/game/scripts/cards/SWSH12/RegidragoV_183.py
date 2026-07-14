from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import is_energy_card


async def celestial_roar(ctx):
    """Discard the top 3 cards of your deck; attach any Energy among them."""
    top = ctx.deck_top(3)
    await ctx.discard_cards(top)
    for card in top:
        if is_energy_card(card):
            await ctx.attach_energy(card, ctx.source)


card = PokemonCardDef(
    guid="7a47f11e-9717-5996-8a0f-bf8ffe530489",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegidragoV.Name",
    display_name="Regidrago V",
    searchable_by=["Regidrago V", "Basic", "V", "RegidragoV"],
    subtypes=["Basic", "V"],
    collector_number=183,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=895,
    abilities=[
        Attack(
            title="Celestial Roar",
            game_text="Discard the top 3 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=celestial_roar,
        ),
        Attack(
            title="Dragon Laser",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.FIRE: 1},
            damage=130,
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)