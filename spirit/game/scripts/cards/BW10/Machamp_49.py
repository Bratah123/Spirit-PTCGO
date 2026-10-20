from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon


class _BadgeOfDisciplinePassive(Passive):
    """The damage of each of your Fighting Pokemon's attacks isn't affected by Resistance."""

    def modify_resistance(self, calc, carrier):
        attacker = calc.attacker
        if (calc.is_attack and attacker is not None
                and attacker.owning_player_id == carrier.owning_player_id
                and PokemonTypes.FIGHTING.value in (attacker.get_attribute(AttrID.POKEMON_TYPES) or [])):
            calc.resistance_applies = False


class _TakesMorePassive(Passive):
    """During your opponent's next turn, damage done to this Pokemon by attacks
    is increased by N (after Weakness and Resistance)."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.target is carrier_pokemon(carrier) and calc.amount > 0:
            calc.amount += self.amount


async def _close_combat(ctx):
    """Printed damage; flip a coin. If tails, during your opponent's next turn
    damage done to this Pokemon by attacks is increased by 30 (after W/R)."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and not results[0]:
        ctx.add_passive_through_opponents_turn(ctx.attacker, _TakesMorePassive(30))


card = PokemonCardDef(
    guid="08bc8462-2a4f-5aec-b25e-00d00b574810",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=49,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Badge of Discipline",
            game_text="The damage of each of your Fighting Pok\u00e9mon's attacks isn't affected by Resistance.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_BadgeOfDisciplinePassive(),
        ),
        Attack(
            title="Close Combat",
            game_text="Flip a coin. If tails, during your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is increased by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=_close_combat,
        ),
    ],
)