from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.session.passives import Passive, carrier_pokemon


class _AllergicShock(Passive):
    """Your next turn: if this Pokemon is damaged by an attack, it is Knocked Out."""
    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if calc.is_attack and calc.amount > 0 and calc.target is me:
            calc.amount = max(calc.amount, me.get_attribute(AttrID.HP, 0))


async def _allergic_shock(ctx):
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_own_next_turn(d, _AllergicShock())


card = PokemonCardDef(
    guid="b78e8f3c-6880-5b63-9c91-879ce3e27de8",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="XY5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Allergic Shock",
            game_text="During your next turn, if the Defending Pok\u00e9mon is damaged by an attack, it is Knocked Out.",
            cost={PokemonTypes.GRASS: 1},
            effect=_allergic_shock,
        ),
        Attack(
            title="Twineedle",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(2, per_heads=50),
        ),
    ],
)