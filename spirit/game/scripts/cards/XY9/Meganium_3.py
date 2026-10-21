from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon


async def gulp_down(ctx):
    """Heal from this Pokémon the same amount of damage you did to your
    opponent's Active Pokémon."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)


class _Overgrow(Passive):
    """With 50 HP or less remaining, this Pokemon's attacks do 70 more to the opponent's Active."""
    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if (me is not None and calc.attacker is me and calc.is_attack and calc.is_opposing
                and calc.to_active and me.get_attribute(AttrID.HP, 0) <= 50):
            calc.amount += 70


card = PokemonCardDef(
    guid="d96a906a-effe-584e-a63a-aadc9fbc8684",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Overgrow",
            game_text="If this Pok\u00e9mon's remaining HP is 50 or less, its attacks do 70 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=_Overgrow(),
        ),
        Attack(
            title="Green Force",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=gulp_down,
        ),
    ],
)